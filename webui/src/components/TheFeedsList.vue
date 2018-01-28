<template>
  <div id="feeds-list">
    <modal v-bind:type="type"></modal>
    <div class="title-container">
      <h1 class="title list-title">Feeds</h1>
      <a href="#" class="button title-button" v-on:click="show_add_modal">
        <i class="fa fa-plus" aria-hidden="true"></i>
        &nbsp;Add
      </a>
    </div>
    <table class="table is-striped">
      <thead>
      <tr>
        <th>ID</th>
        <th>Title</th>
        <th>Last Check</th>
        <th>Last Add</th>
        <th>Save Path</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="feed in feeds" :key="feed.id">
        <td>{{ feed.id }}</td>
        <td>
          <a href="#" class="feed-title" v-on:click="show_update_modal(feed.id)">
            {{ feed.title }}
          </a>
        </td>
        <td>{{ feed.last_check }}</td>
        <td>{{ feed.last_add }}</td>
        <td>{{ feed.save_path }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import Modal from './TheFeedsListModal'
export default {
  name: 'feeds-list',
  data () {
    return {
      type: 'add'
    }
  },
  created () {
    this.$store.dispatch('updateFeeds')
  },
  methods: {
    show_add_modal () {
      this.type = 'add'
      this.$store.dispatch('clearModalToAdd')
        .then(this.$store.dispatch('toggleShowModal'))
    },
    show_update_modal (id) {
      this.type = 'update'
      this.$store.dispatch('setModalToUpdate', id)
        .then(this.$store.dispatch('toggleShowModal'))
    },
    change_update_state: function () {
      this.update_show = !this.update_show
    },
    update: function () {
      this.update_feed_data.keywords = JSON.stringify(this.update_feed_data.keywords)
      this.$http.post('feeds', this.update_feed_data, {'Content-Type': 'application/json'})
        .then((response) => {
          if (response.body === 'OK') {
            location.reload()
          }
        })
    }
  },
  computed: {
    feeds () {
      return this.$store.getters.getAllFeeds
    }
  },
  components: {
    'modal': Modal
  }
}
</script>

<style scoped>
.title-container {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.title-button {
  margin-left: 1rem;
}
.feed-title {
  color: #000;
}
.list-title {
  margin-top: 1.5rem;
}
table {
  width: 100%;
}
</style>
