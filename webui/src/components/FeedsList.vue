<template>
  <div id="feeds-list">
    <div class="modal" v-bind:class="{ 'is-active': update_show }">
      <div class="modal-background"></div>
      <div class="modal-content">
        <div class="card">
          <p class="card-header-title">
            Update Feed
          </p>
          <div class="card-content">
            <div class="field">
              <label class="label">Title</label>
              <div class="control">
                <input class="input" type="text" v-model="update_feed_data.title">
              </div>
            </div>
            <div class="field">
              <label class="label">URL</label>
              <div class="control">
                <input class="input" type="text" v-model="update_feed_data.url">
              </div>
            </div>
            <div class="field">
              <label class="label">Save Path</label>
              <div class="control">
                <input class="input" type="text" v-model="update_feed_data.save_path">
              </div>
            </div>
            <div class="field">
              <label class="label">Keywords</label>
              <p v-for="keyword in update_feed_data.keywords" :key="keyword">
                {{ keyword }}
              </p>
              <div class="keyword-container">
                <div class="control">
                  <input class="input" type="text" v-model="update_keyword">
                </div>
                <a href="#" class="add-button" v-on:click="add_and_clear_update_keyword">
                  <i class="fa fa-plus-circle" aria-hidden="true"></i>
                </a>
              </div>
            </div>
            <a href="#" class="button" v-on:click="update">Update</a>
          </div>
        </div>
      </div>
      <button class="modal-close is-large" aria-label="close" v-on:click="change_update_state"></button>
    </div>
    <div class="modal" v-bind:class="{ 'is-active': add_show }">
      <div class="modal-background"></div>
      <div class="modal-content">
        <div class="card">
          <p class="card-header-title">
            Add New Feed
          </p>
          <div class="card-content">
            <div class="field">
              <label class="label">Title</label>
              <div class="control">
                <input class="input" type="text" v-model="add_feed_data.title">
              </div>
            </div>
            <div class="field">
              <label class="label">URL</label>
              <div class="control">
                <input class="input" type="text" v-model="add_feed_data.url">
              </div>
            </div>
            <div class="field">
              <label class="label">Save Path</label>
              <div class="control">
                <input class="input" type="text" v-model="add_feed_data.save_path">
              </div>
            </div>
            <div class="field">
              <label class="label">Keywords</label>
              <p v-for="keyword in add_feed_data.keywords" :key="keyword">
                {{ keyword }}
              </p>
              <div class="keyword-container">
                <div class="control">
                  <input class="input" type="text" v-model="add_keyword">
                </div>
                <a href="#" class="add-button" v-on:click="add_and_clear_keyword">
                  <i class="fa fa-plus-circle" aria-hidden="true"></i>
                </a>
              </div>
            </div>
            <a href="#" class="button" v-on:click="submit">Submit</a>
          </div>
        </div>
      </div>
      <button class="modal-close is-large" aria-label="close" v-on:click="change_show_state"></button>
    </div>
    <div class="title-container">
      <h1 class="title list-title">Feeds</h1>
      <a href="#" class="button title-button" v-on:click="change_show_state">
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
          <a href="#" class="feed-title" v-on:click="show_update(feed.id)">
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
  export default {
    name: 'feeds-list',
    data() {
      return {
        feeds: [],
        add_show: false,
        add_feed_data: {
          title: 'Default title',
          url: '',
          save_path: '',
          keywords: []
        },
        add_keyword: "",
        update_show: false,
        update_feed_data: {
          id: '',
          title: '',
          url: '',
          save_path: '',
          keywords: []
        },
        update_keyword: ""
      }
    },
    created() {
      this.$http.get('feeds')
      .then(response => response.json())
      .then((json) => {
        this.feeds = json
      })
    },
    methods: {
      change_show_state: function () {
        this.add_show = !this.add_show
        this.add_feed_data = {
          title: 'Default title',
          url: '',
          save_path: '',
          keywords: []
        }
      },
      add_and_clear_keyword: function () {
        this.add_feed_data.keywords.push(this.add_keyword)
        this.add_keyword = ""
      },
      add_and_clear_update_keyword: function () {
        this.update_feed_data.keywords.push(this.update_keyword)
        this.update_keyword = ""
      },
      submit: function () {
        this.$http.post('feeds', this.add_feed_data, {'Content-Type': 'application/json'})
          .then((response) => {
          if (response.body === 'OK'){
            location.reload()
          }
        })
      },
      show_update: function (id) {
        this.click_feed_id = id
        for (const feed of this.feeds) {
          if (feed.id === id) {
            this.update_feed_data = JSON.parse(JSON.stringify(feed))
            delete this.update_feed_data.last_add
            delete this.update_feed_data.last_check
            delete this.update_feed_data.create_time
            break
          }
        }
        this.change_update_state()
      },
      change_update_state: function () {
        this.update_show = !this.update_show
      },
      update: function() {
        this.update_feed_data.keywords = JSON.stringify(this.update_feed_data.keywords)
        this.$http.post('feeds', this.update_feed_data, {'Content-Type': 'application/json'})
        .then((response) => {
          if (response.body === 'OK') {
            location.reload()
          }
        })
      }
    }
  }
</script>

<style>
  .title-container {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .title-button {
    margin-left: 1rem;
  }

  .keyword-container {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .add-button {
    margin-left: 1rem;
    color: #000;
  }

  .feed-title {
    color: #000;
  }
</style>

