import Vuex from 'vuex'
import Vue from 'vue'
import actions from './actions'
import mutations from './mutations'

Vue.use(Vuex)

const state = {
  feeds: [],
  items: [],
  show_modal: false,
  modal_feed: {}
}

const getters = {
  getFeedByID: (state) => (id) => {
    return state.feeds.find(feed => feed.id === id)
  },
  getAllItems: (state) => {
    return state.items
  },
  getAllFeeds: (state) => {
    return state.feeds
  }
}

export default new Vuex.Store({
  state,
  mutations,
  getters,
  actions
})
