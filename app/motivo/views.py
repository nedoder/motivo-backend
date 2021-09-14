from rest_framework import viewsets
from .serializers import UserSerializer, ProfileSerializer, ChallengeSerializer, CompletedSerializer, AttemptSerializer, UserEditSerializer, AwardsSerializer, PostAttemptSerializer, UserDataSerializer, CollectedAwardsSerializer, UsersCollectedAwardsSerializer
from .models import Profile, Challenge, Attempt, Awards, CollectedAwards
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from django.core import mail
from django.core.mail import EmailMessage
from django.template.loader import get_template


class Mailer:
    """
    Send email messages helper class
    """

    def __init__(self, from_email=None):
        # TODO setup the default from email
        self.connection = mail.get_connection()
        self.from_email = from_email

    def send_messages(self, subject, template, context, to_emails):
        messages = self.__generate_messages(subject, template, context, to_emails)
        self.__send_mail(messages)

    def __send_mail(self, mail_messages):
        """
        Send email messages
        :param mail_messages:
        :return:
        """
        self.connection.open()
        self.connection.send_messages(mail_messages)
        self.connection.close()

    def __generate_messages(self, subject, template, context, to_emails):
        """
        Generate email message from Django template
        :param subject: Email message subject
        :param template: Email template
        :param to_emails: to email address[es]
        :return:
        """
        messages = []
        message_template = get_template(template)
        for recipient in to_emails:
            message_content = message_template.render(context)
            message = EmailMessage(subject, message_content, to=[recipient], from_email=self.from_email)
            message.content_subtype = 'html'
            messages.append(message)

        return messages


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all().order_by('initial_budget_gross')
    serializer_class = UserSerializer

class UserDataViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserDataSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return User.objects.filter(id=user.id)
        raise PermissionDenied()

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class RankingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all().order_by('-collected_coins_gross')
    serializer_class = UserSerializer

class ChallengeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Challenge.objects.all().order_by('title')
    serializer_class = ChallengeSerializer

class CompletedViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Attempt.objects.all().filter(confirmed_by_admin=True).order_by('date')
    serializer_class = CompletedSerializer


class AttemptViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Attempt.objects.all().filter(confirmed_by_admin=False)
    serializer_class = AttemptSerializer

    def create(self, request, *args, **kwargs):
        serializer = PostAttemptSerializer(data=request.data)
        if serializer.is_valid():
            mail = Mailer()
            mail.send_messages(subject='Attempting the challenge',
                               template='emails/customer_verification.html',
                               context={'customer': self},
                               to_emails=[self.user.email])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserEditViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserEditSerializer

class AwardsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer

class UsersAwardsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CollectedAwards.objects.all()
    serializer_class = UsersCollectedAwardsSerializer


class CollectedAwardsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CollectedAwards.objects.all()
    serializer_class = CollectedAwardsSerializer

    def create(self, request, *args, **kwargs):
        serializer = CollectedAwardsSerializer(data=request.data)
        if serializer.is_valid():
            user = request.data.get("user")
            print('------')
            print(user)
            print('------')
            profile = Profile.objects.get(user_id = user)
            awards = request.data.get("awards")
            award = Awards.objects.get(id = awards)
            print(awards)
            if profile.collected_coins >= award.price_in_coins:
                profile.collected_coins = profile.collected_coins - award.price_in_coins
                profile.save()
                serializer.save()
                return Response({"message":"You got the award"}, status=status.HTTP_201_CREATED)
        print(awards)
        return Response({"message":"You have not enough coins"}, status=status.HTTP_400_BAD_REQUEST)

class DisplayImageView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, imagename):
        """
        Endpoint displays particular image.
        """
        image_path = f'uploads/images/{imagename}'
        image_data = open(image_path, "rb").read()
        return HttpResponse(image_data, content_type="image/*")