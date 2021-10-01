<template>
    <div>
        <!-- <CRow>
            <CCardBody color="white" class="mb-4">
                <CCol sm="12">
                    <h1 class="text-center font-weight-bold">Progress</h1>
                    <p>Percentage of challenges that you attempted:</p>
                    <CProgress :value="countRate" color="info" showPercentage=True animated show-value style="height:40px;" />
                </CCol>
            </CCardBody>
        </CRow> -->
        <CRow>
            <CCol sm='4'>
                <!-- <Title text="To do" class="font-weight-bold" :number="toDo" activeColor="dark" v-bind:style="{borderRadius: '18px', border: '2px solid #EBEDF0'}"/> -->
                <div v-for="challenge in challenges"  @click="challenge.attempts_left===0 ? null : taskClicked(challenge)" class="challenge_card challenge" :style= "[challenge.attempts_left===0 ? {background:'rgba(153,162,173, 0.2)'} : {background:'transparent'}]">
                    <h1>{{challenge.title}}</h1>
                     <h6>Attempts left: {{challenge.attempts_left}}</h6>
                    <p v-linkified>{{challenge.description}}</p>
                    <p class='coin_text'> {{challenge.coins_to_win  }} &nbsp;   <img class="text-info" src="./img/Coin.png"/></p>
                    <button class="btn btn-info disabled"> To do</button>
                </div>
            </CCol>
            <CCol sm='4'>
                <!-- <Title text="In progress" class="font-weight-bold" :number="failed" activeColor="dark" v-bind:style="{borderRadius: '18px', border: '2px solid #EBEDF0'}" /> -->
                <div v-for="attempt in attempts" @click="attemptClicked(attempt.challenge)" class="challenge_card">
                    <h1>{{attempt.challenge.title}}</h1>
                    <p v-linkified>{{attempt.description}} </p>
                    <p class="coin_text">{{attempt.challenge.coins}} &nbsp;   <img class="text-info" src="./img/Coin.png"/></p>
                     <button class="btn btn-danger disabled"> In progress</button>
                </div>
            </CCol>
            <CCol sm='4'>
                <!-- <Title text="Done" class="font-weight-bold" :number="passed" activeColor="dark" v-bind:style="{borderRadius: '18px', border: '2px solid #EBEDF0'}" /> -->
                <div v-for="complet in complets"  class="challenge_card" @click="completedClicked(complet.challenge)" v-bind:style="{borderRadius: '18px'}">
                    <h1>{{complet.challenge.title}}</h1>
                    <p v-linkified>{{complet.challenge.description}}</p>
                    <p class="coin_text">{{complet.challenge.coins}} &nbsp;   <img class="text-info" src="./img/Coin.png"/> </p>
                     <button class="btn btn-success disabled"> Done</button>
                </div>
            </CCol>
        </CRow>
    </div>
</template>

<script>
    import Title from './elements/Title.vue';
    import TheHeader from '../../containers/TheHeader.vue'
    import axios from 'axios'
    
   console.log("Siema!");

    export default {
        name: 'Challenges',
        components: {
            Title,
            TheHeader
        },
        data() {
            return {
                challenges: [],
                attempts: [],
                complets: [],
                toDo: null,
                failed: null,
                passed: null,
                counter: null,
            }
        },
         computed: {
      computedItems() {
         
        return this.complets.map(item => {
          return {
            ...item,
            challengeTitle: item.challenge.title,
          
            //userId: item.user.id
          }
        })
        
      }},
        mounted() {
            const token = localStorage.getItem('user-token')
            const bearer = 'Bearer ' + token
            const challenges = axios({
                method: 'get',
                url: 'https://api.motivo.localhost/challenges/',
                headers: {
                    'Authorization': bearer,
                }
            });

            const attempts = axios({
                method: 'get',
                url: 'https://api.motivo.localhost/attempt/',
                headers: {
                    'Authorization': bearer,
                }
            });

            const complets = axios({
                method: 'get',
                url: 'https://api.motivo.localhost/completed/',
                headers: {
                    'Authorization': bearer,
                }
            });

            Promise.all([challenges, attempts, complets]).then(([chal, att, com]) => {
                this.attempts = att.data.results;
                this.failed = att.data.results.length;
                this.challenges = chal.data;
                 this.challenges.sort(function (a, b) {
              return a.attempts_left - b.attempts_left
        })
                this.toDo = chal.data.length;
                this.complets = com.data.results;
                this.passed = com.data.results.length;
                console.log(this.complets)
                console.log(com.data)
            }).catch(error => console.log(error));

        },
        watch: {
            $route: {
                immediate: true,
                handler(route) {
                    if (route.query && route.query.page) {
                        this.activePage = Number(route.query.page)
                    }
                }
            }
        },
        methods: {
            //     getBadge (status) {
            //       switch (status) {
            //         case 'Active': return 'success'
            //         case 'Inactive': return 'secondary'
            //         case 'Pending': return 'warning'
            //         case 'Banned': return 'danger'
            //         default: 'primary'
            //       }
            //     },
            taskClicked(challenge) {
                this.$router.push({
                    path: `/dashboard/challenges/${challenge.id}`
                })
            },
            completedClicked(completed) {
                this.$router.push({
                    path: `/dashboard/challenges/completed/${completed.id}`
                })
            },
             attemptClicked(attempt) {
                this.$router.push({
                    path: `/dashboard/challenges/attempt/${attempt.id}`
                })
            },


            //     pageChange (val) {
            //       this.$router.push({ query: { page: val }})
            //     }
        },
        computed: {
            countRate: function() {
                return Math.round(this.toDo/(this.failed+this.toDo+this.passed)*100)}
        }
    }
</script>

<style scoped>

h1 {
font-size: 36px;
color: #03001D;
word-wrap: break-word;
}

.challenge_card {
border: 2px solid #EBEDF0;
box-shadow: 0px 2px 0px #CFD8DA;
border-radius: 18px;
padding: 15px;
margin-top: 25px;
height: 250px;
display: flex;
flex-direction: column; 
justify-content: space-around;
}

.disabled {
    width: 50% !important;
}

.challenge_card:hover {
    background-color: rgba(153,162,173, 0.2) !important;
    cursor: pointer;
}

p:first-child {
    color: #6D7885;
    font-size: 16px;
}

.coin_text {
color: #F2C94C;    
font-weight: bold;
font-size: 24px;
display: flex;
align-items: center;
justify-content: left;
}

</style>