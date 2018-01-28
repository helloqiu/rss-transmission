import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

const state = {
  feeds: [],
  items: [],
  show_modal: false,
  modal_feed: {}
}

const mutations = {
  setFeeds (state, feeds) {
    state.feeds = feeds
  },
  setItems (state, items) {
    state.items = items
  },
  setShowModal (state, showState) {
    state.show_modal = showState
  },
  setModalFeed (state, feed) {
    state.modal_feed = feed
  }
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

const actions = {
  updateFeeds ({ commit }) {
    Vue.http.get('feeds')
      .then(response => response.json())
      .then((json) => {
        commit('setFeeds', json)
      })
  },
  updateItems ({ commit }) {
    Vue.http.get('items')
      .then(response => response.json())
      .then((json) => {
        commit('setItems', json)
      })
  },
  toggleShowModal ({ commit, state }) {
    commit('setShowModal', !state.show_modal)
  },
  clearModalToAdd ({ commit }) {
    return new Promise((resolve, reject) => {
      commit('setModalFeed', {
        title: 'Default title',
        url: '',
        save_path: '',
        keywords: []
      })
    })
  },
  setModalToUpdate ({ commit, getters }, id) {
    return new Promise((resolve, reject) => {
      commit('setModalFeed', getters.getFeedByID(id))
    })
  },
  postFeed () {
    const temp = JSON.parse(JSON.stringify(state.modal_feed))
    if (temp.hasOwnProperty('create_time')) {
      delete temp['create_time']
    }
    if (temp.hasOwnProperty('last_check')) {
      delete temp['last_check']
    }
    if (temp.hasOwnProperty('last_add')) {
      delete temp['last_add']
    }
    Vue.http.post('feeds', temp, {'Content-Type': 'application/json'})
      .then((response) => {
        if (response.body === 'OK') {
          location.reload()
        }
      })
  }
}

export default new Vuex.Store({
  state,
  mutations,
  getters,
  actions
})
