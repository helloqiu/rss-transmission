import Vue from 'vue'

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
      const temp = JSON.parse(JSON.stringify(getters.getFeedByID(id)))
      commit('setModalFeed', temp)
    })
  },
  postFeed ({ state }) {
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
    temp.keywords = JSON.stringify(temp.keywords)
    Vue.http.post('feeds', temp, {'Content-Type': 'application/json'})
      .then((response) => {
        if (response.body === 'OK') {
          location.reload()
        }
      })
  },
  deleteKeyword ({ commit }, keyword) {
    commit('deleteKeyword', keyword)
  },
  deleteFeedByID ({ state }, id) {
    Vue.http.delete('feeds',
      {'Content-Type': 'application/json', 'params': {id}}
    )
      .then(response => {
        if (response.body === 'OK') {
          location.reload()
        }
      })
  }
}

export default actions
