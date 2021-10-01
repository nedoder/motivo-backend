import Vue from 'vue'
import Router from 'vue-router'
import axios from 'axios'

// Containers
const TheContainer = () =>
    import ('@/containers/TheContainer')


// Views
// @todo please use webpackChunkName and group modules by group, for example group-auth, group-users, group-some-module
const Dashboard = () =>
    import ( /* webpackChunkName: "group-dashboard" */ '@/views/Dashboard')


// @todo please delete this routes, you can leave pages, maybe users
// const Colors = () =>
//     import ('@/views/theme/Colors')
// const Typography = () =>
//     import ('@/views/theme/Typography')

const CustomLogIn = () =>
    import ('@/views/pages/CustomLogIn')

const ChangePassword = () =>
    import ('@/views/pages/ChangePassword')

const Onboarding1 = () =>
    import ('@/views/pages/Onboarding1')

const Onboarding2 = () =>
    import ('@/views/pages/Onboarding2')

const Onboarding3 = () =>
    import ('@/views/pages/Onboarding3')

const Onboarding4 = () =>
    import ('@/views/pages/Onboarding4')

const Onboarding5 = () =>
    import ('@/views/pages/Onboarding5')

const Edit = () =>
    import ('@/views/pages/Edit')

const Profile = () =>
    import ('@/views/pages/Profile')

const Ranking = () =>
    import ('@/views/pages/Ranking')

//pages that we need @oliwia

const Awards = () =>
    import ('@/views/pages/Awards')

const Award = () =>
    import ('@/views/pages/Award')

const Tests = () =>
    import ('@/views/pages/Tests')

const CustomSignUp = () =>
    import ('@/views/pages/CustomSignUp')


const Page404 = () =>
    import ('@/views/pages/Page404')

const Page500 = () =>
    import ('@/views/pages/Page500')

const Login = () =>
    import ('@/views/pages/Login')

const Register = () =>
    import ('@/views/pages/Register')

const Challenges = () =>
    import ('@/views/pages/Challenges')

const Challenge = () =>
    import ('@/views/pages/Challenge')

const Completed = () =>
    import ('@/views/pages/Completed')

const Attempt = () =>
    import ('@/views/pages/Attempt')

const UserInfo = () =>
    import ('@/views/pages/UserInfo')

// const Charts = () =>
//     import ('@/views/charts/Charts')
// const Widgets = () =>
//     import ('@/views/widgets/Widgets')

// Views - Components
// const Cards = () =>
//     import ('@/views/base/Cards')
// const Forms = () =>
//     import ('@/views/base/Forms')
// const Switches = () =>
//     import ('@/views/base/Switches')
// const Tables = () =>
//     import ('@/views/base/Tables')
// const Tabs = () =>
//     import ('@/views/base/Tabs')
// const Breadcrumbs = () =>
//     import ('@/views/base/Breadcrumbs')
// const Carousels = () =>
//     import ('@/views/base/Carousels')
// const Collapses = () =>
//     import ('@/views/base/Collapses')
// const Jumbotrons = () =>
//     import ('@/views/base/Jumbotrons')
// const ListGroups = () =>
//     import ('@/views/base/ListGroups')
// const Navs = () =>
//     import ('@/views/base/Navs')
// const Navbars = () =>
//     import ('@/views/base/Navbars')
// const Paginations = () =>
//     import ('@/views/base/Paginations')
// const Popovers = () =>
//     import ('@/views/base/Popovers')
// const ProgressBars = () =>
//     import ('@/views/base/ProgressBars')
// const Tooltips = () =>
//     import ('@/views/base/Tooltips')

// Views - Buttons
const StandardButtons = () =>
    import ('@/views/buttons/StandardButtons')
const ButtonGroups = () =>
    import ('@/views/buttons/ButtonGroups')
const Dropdowns = () =>
    import ('@/views/buttons/Dropdowns')
const BrandButtons = () =>
    import ('@/views/buttons/BrandButtons')

// Views - Icons
const CoreUIIcons = () =>
    import ('@/views/icons/CoreUIIcons')
const Brands = () =>
    import ('@/views/icons/Brands')
const Flags = () =>
    import ('@/views/icons/Flags')

// Views - Notifications
const Alerts = () =>
    import ('@/views/notifications/Alerts')
const Badges = () =>
    import ('@/views/notifications/Badges')
const Modals = () =>
    import ('@/views/notifications/Modals')


// Users
const Users = () =>
    import ('@/views/pages/elements/users/Users')
const User = () =>
    import ('@/views/pages/elements/users/User')

Vue.use(Router)

export default new Router({
    mode: 'hash', // https://router.vuejs.org/api/#mode
    linkActiveClass: 'active',
    scrollBehavior: () => ({
        y: 0
    }),
    routes: configRoutes()
})

function configRoutes() {
    return [{
            path: '/',
            //redirect: '/dashboard',
            name: 'CustomLogin',
            component: CustomLogIn,
        },
        {
            path: '/edit',
            //redirect: '/dashboard',
            name: 'Edit',
            component: Edit,
        },
        {
            path: '/onboarding1',
            //redirect: '/dashboard',
            name: 'Onboarding1',
            component: Onboarding1,
        },
        {
            path: '/changepassword',
            //redirect: '/dashboard',
            name: 'ChangePassword',
            component: ChangePassword,
        },
        {
            path: '/onboarding2',
            //redirect: '/dashboard',
            name: 'Onboarding2',
            component: Onboarding2,
        },
        {
            path: '/onboarding3',
            //redirect: '/dashboard',
            name: 'Onboarding3',
            component: Onboarding3,
        },
        {
            path: '/onboarding4',
            //redirect: '/dashboard',
            name: 'Onboarding4',
            component: Onboarding4,
        },
        {
            path: '/onboarding5',
            //redirect: '/dashboard',
            name: 'Onboarding5',
            component: Onboarding5,

        },
        {
            path: '/profile',
            //redirect: '/dashboard',
            name: 'Profile',
            component: Profile,
        },

        {
            path: '/awards',
            //redirect: '/dashboard',
            name: 'awards',
            component: Awards,
        },
        // {
        //     path: '/tasks',
        //     //redirect: '/dashboard',
        //     name: 'Tasks',
        //     component: Tasks,
        // },
        {
            path: '/ranking',
            //redirect: '/dashboard',
            name: 'Ranking',
            component: Ranking,
        },
        {
            path: '/tests',
            //redirect: '/dashboard',
            name: 'Tests',
            component: Tests,
        },
        {
            path: '/dashboard',
            //redirect: '/dashboard',
            name: 'Home',
            component: TheContainer,
            children: [{
                    path: 'dashboard',
                    name: 'Dashboard',
                    component: Dashboard
                },
                {
                    path: 'UserInfo',
                    meta: {
                        label: 'UserInfo'
                    },
                    component: {
                        render(c) {
                            return c('router-view')
                        }
                    },
                    children: [{
                        path: '',
                        name: 'UserInfo',
                        component: UserInfo
                    }, ]
                },
                {
                    path: 'awards',
                    meta: {
                        label: 'awards'
                    },
                    component: {
                        render(c) {
                            return c('router-view')
                        }
                    },
                    children: [{
                            path: '',
                            name: 'awards',
                            component: Awards
                        },
                        {
                            path: ':id',
                            meta: {
                                label: 'awards'
                            },
                            name: 'awards',
                            component: Award
                        },
                    ]
                },
                {
                    path: 'Ranking',
                    meta: {
                        label: 'Ranking'
                    },
                    component: {
                        render(c) {
                            return c('router-view')
                        }
                    },
                    children: [{
                        path: '',
                        name: 'Ranking',
                        component: Ranking
                    }, ]
                },
                {
                    path: 'users',
                    meta: {
                        label: 'Users'
                    },
                    component: {
                        render(c) {
                            return c('router-view')
                        }
                    },
                    children: [{
                            path: '',
                            name: 'Users',
                            component: Users
                        },
                        {
                            path: ':id',
                            meta: {
                                label: 'User Details'
                            },
                            name: 'User',
                            component: User
                        }
                    ]
                },
                {
                    path: 'changepassword',
                    meta: {
                        label: 'Password'
                    },
                    component: {
                        render(c) {
                            return c('router-view')
                        }
                    },
                    children: [{
                        path: '',
                        name: 'ChangePassword',
                        component: ChangePassword
                    }, ]
                },
                {
                    path: 'challenges',
                    meta: {
                        label: 'challenges'
                    },
                    component: {
                        render(c) {
                            return c('router-view')
                        }
                    },
                    children: [{
                            path: '',
                            name: 'Challenges',
                            component: Challenges
                        },
                        {
                            path: ':id',
                            meta: {
                                label: 'challenge'
                            },
                            name: 'Challenges',
                            component: Challenge
                        },
                        {
                            path: 'completed/:id',
                            meta: {
                                label: 'Completed'
                            },
                            name: 'Completed',
                            component: Completed
                        },
                        {
                            path: 'attempt/:id',
                            meta: {
                                label: 'Attempt'
                            },
                            name: 'Attempt',
                            component: Attempt
                        }
                    ]
                },



                {
                    path: 'buttons',
                    redirect: '/buttons/standard-buttons',
                    name: 'Buttons',
                    component: {
                        render(c) {
                            return c('router-view')
                        }
                    },
                    children: [{
                            path: 'standard-buttons',
                            name: 'Standard Buttons',
                            component: StandardButtons
                        },
                        {
                            path: 'button-groups',
                            name: 'Button Groups',
                            component: ButtonGroups
                        },
                        {
                            path: 'dropdowns',
                            name: 'Dropdowns',
                            component: Dropdowns
                        },
                        {
                            path: 'brand-buttons',
                            name: 'Brand Buttons',
                            component: BrandButtons
                        }
                    ]
                },
                {
                    path: 'icons',
                    redirect: '/icons/coreui-icons',
                    name: 'CoreUI Icons',
                    component: {
                        render(c) {
                            return c('router-view')
                        }
                    },
                    children: [{
                            path: 'coreui-icons',
                            name: 'Icons library',
                            component: CoreUIIcons
                        },
                        {
                            path: 'brands',
                            name: 'Brands',
                            component: Brands
                        },
                        {
                            path: 'flags',
                            name: 'Flags',
                            component: Flags
                        }
                    ]
                },
                {
                    path: 'notifications',
                    redirect: '/notifications/alerts',
                    name: 'Notifications',
                    component: {
                        render(c) {
                            return c('router-view')
                        }
                    },
                    children: [{
                            path: 'alerts',
                            name: 'Alerts',
                            component: Alerts
                        },
                        {
                            path: 'badges',
                            name: 'Badges',
                            component: Badges
                        },
                        {
                            path: 'modals',
                            name: 'Modals',
                            component: Modals
                        }
                    ]
                }
            ]
        },
        {
            path: '/pages',
            redirect: '/pages/404',
            name: 'Pages',
            component: {
                render(c) {
                    return c('router-view')
                }
            },
            children: [{
                    path: '404',
                    name: 'Page404',
                    component: Page404
                },
                {
                    path: '500',
                    name: 'Page500',
                    component: Page500
                },
                {
                    path: 'login',
                    name: 'Login',
                    component: Login
                },
                {
                    path: 'register',
                    name: 'Register',
                    component: Register
                }
            ]
        }
    ]
}

axios.interceptors.response.use(response => {
    return response
}, error => {
    if (error.response.status === 401) {
        axios({
                method: 'post',
                url: 'https://api.motivo.localhost/api/token/refresh/',
                data: { refresh: localStorage.getItem('user-refresh') },
            })
            .then(
                resp => {
                    localStorage.setItem('user-token', resp.data.access)
                }
            )
            .catch(error => console.log(error))
    } else {
        return Promise.reject(error)
    }
})