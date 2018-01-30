<template>
  <div class="modal" v-bind:class="{ 'is-active': show }" id='the-feeds-list-modal'>
    <div class="modal-background"></div>
    <div class="modal-content">
      <div class="card">
        <p class="card-header-title">
          {{ title }}
        </p>
        <div class="card-content">
          <div class="field">
            <label class="label">Title</label>
            <div class="control">
              <input class="input" type="text" v-model="feed.title">
            </div>
          </div>
          <div class="field">
            <label class="label">URL</label>
            <div class="control">
              <input class="input" type="text" v-model="feed.url">
            </div>
          </div>
          <div class="field">
            <label class="label">Save Path</label>
            <div class="control">
              <input class="input" type="text" v-model="feed.save_path">
            </div>
          </div>
          <div class="field">
            <label class="label">Keywords</label>
            <p v-for="keyword in feed.keywords" :key="keyword">
              {{ keyword }}
              <a href="#" class="delete-button" v-on:click="delete_keyword(keyword)">
                <i class="fa fa-minus-circle" aria-hidden="true"></i>
              </a>
            </p>
            <div class="keyword-container">
              <div class="control">
                <input class="input" type="text" v-model="keyword">
              </div>
              <a href="#" class="add-button" v-on:click="add_and_clear_keyword">
                <i class="fa fa-plus-circle" aria-hidden="true"></i>
              </a>
            </div>
          </div>
          <a href="#" class="button" v-on:click="commit">{{ action }}</a>
          <a href="#" class="button is-danger is-outlined" v-if="type === 'update'" v-on:click="delete_feed">
            Delete
          </a>
        </div>
      </div>
    </div>
  <button class="modal-close is-large" aria-label="close" v-on:click="close"></button>
  </div>
</template>

<script>
export default {
  name: 'the-feeds-list-modal',
  data () {
    return {
      keyword: ''
    }
  },
  methods: {
    add_and_clear_keyword () {
      this.feed.keywords.push(this.keyword)
      this.keyword = ''
    },
    commit () {
      this.$store.dispatch('postFeed')
    },
    close () {
      this.$store.dispatch('toggleShowModal')
    },
    delete_keyword (keyword) {
      this.$store.dispatch('deleteKeyword', keyword)
    },
    delete_feed () {
      this.$store.dispatch('deleteFeedByID', this.feed.id)
    }
  },
  props: [
    'type'
  ],
  computed: {
    title () {
      if (this.type === 'update') {
        return 'Update Feed'
      }
      if (this.type === 'add') {
        return 'Add New Feed'
      }
      return ''
    },
    action () {
      if (this.type === 'update') {
        return 'Update'
      }
      if (this.type === 'add') {
        return 'Add'
      }
      return ''
    },
    show () {
      return this.$store.state.show_modal
    },
    feed: {
      get () {
        return this.$store.state.modal_feed
      },
      set (value) {
        this.$store.commit('setModalFeed', value)
      }
    }
  }
}
</script>

<style scoped>
.keyword-container {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.add-button {
  margin-left: 1rem;
  color: #000;
}
.delete-button {
  margin-left: 0.5rem;
  color: #000;
}
</style>
