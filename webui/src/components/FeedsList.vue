<template>
  <div id="feeds-list">
    <h1 class="title list-title">Feeds</h1>
    <a href="#" class="button">Add</a>
    <table class="table is-striped">
      <thead>
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Create Time</th>
          <th>Save Path</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="feed in feeds" :key="feed.id">
          <td>{{ feed.id }}</td>
          <td>{{ feed.title }}</td>
          <td>{{ feed.create_time }}</td>
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


