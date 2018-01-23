<template>
  <div id="feeds-list">
    <div class="title-container">
      <h1 class="title list-title">Feeds</h1>
      <a href="#" class="button title-button">
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
          <td>{{ feed.title }}</td>
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
  data () {
    return {
      feeds: []
    }
  },
  created () {
    this.$http.get('feeds')
    .then(response => response.json())
    .then((json) => {
      this.feeds = json
    })
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
</style>

