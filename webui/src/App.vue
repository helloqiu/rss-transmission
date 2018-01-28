<template>
  <div id="app">
    <navbar></navbar>
    <div class="columns">
      <div class="column is-10 is-offset-1">
        <feeds-list></feeds-list>
        <items-list></items-list>
      </div>
    </div>
  </div>
</template>

<script>
import FeedsList from './components/TheFeedsList'
import ItemsList from './components/TheItemsList'
import Navbar from './components/TheNavbar'

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components: {
    'feeds-list': FeedsList,
    'items-list': ItemsList,
    'navbar': Navbar
  }
}
</script>

<style>
html, body, #app {
  height: 100%;
  width: 100%;
}
</style>
