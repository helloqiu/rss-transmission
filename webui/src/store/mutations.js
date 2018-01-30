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
  },
  deleteKeyword (state, keyword) {
    state.modal_feed.keywords = state.modal_feed.keywords.filter(item => {
      if (item !== keyword) {
        return item
      }
    })
  }
}

export default mutations
