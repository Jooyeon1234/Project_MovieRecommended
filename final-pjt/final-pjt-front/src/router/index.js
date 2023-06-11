import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/movies/MovieList'
import MovieHomeView from '@/views/movies/MovieHomeView'
import RiviewListView from '@/views/reviews/ReviewListView'
import RiviewDetailView from '@/views/reviews/ReviewDetail'
import MovieReView from '@/views/movies/MovieReView'
import DetailView from '@/views/movies/MovieDetail'
import LoginView from '@/views/accounts/LoginView'
import LogoutView from '@/views/accounts/LogoutView'
import SignupView from '@/views/accounts/SignupView'
import CreateReView from '@/views/reviews/CreateReView'
import UpdateReView from '@/views/reviews/UpdateReView'
import ProfileView from '@/views/accounts/ProfileView'
import NotFound404 from '@/views/accounts/NotFound404'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'moviehome',
    component: MovieHomeView,
  },
  {
    path: '/',
    name: 'home',
    component: MovieView,
  },
  {
    path: '/movies/reviewcreate',
    name: 'MovieReView',
    component: MovieReView,
  },
  {
    path: '/reviews',
    name: 'reviews',
    component: RiviewListView,
  },
  {
    path: '/reviews/create',
    name: 'createreviews',
    component: CreateReView,
  },
  {
    path: '/reviews/update',
    name: 'updatereview',
    component: UpdateReView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView,
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView,
  },
  {
    path: '/movies/:id',
    name: 'moviedetail',
    component: DetailView,
  },
  {
    path: '/reviews/:id',
    name: 'reviewdetail',
    component: RiviewDetailView,
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
