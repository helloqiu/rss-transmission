<template>
  <div id="items-list">
    <h1 class="title list-title">Items</h1>
    <table class="table is-striped">
      <thead>
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Publish Time</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.title }}</td>
          <td>{{ item.publish_time }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'items-list',
  data () {
    return {
      items: []
    }
  },
  created () {
    this.$http.get('items')
    .then(response => response.json())
    .then((json) => {
      this.items = json
    })
  }
}
</script>


