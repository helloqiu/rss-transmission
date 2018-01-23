<template>
  <div id="items-list">
    <div class="title-container">
      <h1 class="title list-title">Items</h1>
      <a href="#" class="button title-button" v-on:click="change_show_state">
        <p v-if="!show">
          <i class="fa fa-angle-up" aria-hidden="true"></i>
          &nbsp; show
        </p>
        <p v-else>
          <i class="fa fa-angle-down" aria-hidden="true"></i>
          &nbsp; hide
        </p>
      </a>
    </div>
    <table class="table is-striped" v-if="show">
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
      items: [],
      show: false
    }
  },
  created () {
    this.$http.get('items')
    .then(response => response.json())
    .then((json) => {
      this.items = json
    })
  },
  methods: {
    change_show_state: function () {
      this.show = !this.show
    }
  }
}
</script>


