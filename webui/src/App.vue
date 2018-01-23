<template>
  <div id="app">
    <nav class="navbar has-shadow" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <p class="navbar-item">
          RSS Transmission WEB UI
        </p>
      </div>
    </nav>
    <div class="columns">
      <div class="column is-10 is-offset-1">
        <feeds-list></feeds-list>
        <items-list></items-list>
      </div>
    </div>
  </div>
</template>

<script>
import FeedsList from './components/FeedsList'
import ItemsList from './components/ItemsList'

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components: {
    'feeds-list': FeedsList,
    'items-list': ItemsList
  }
}
</script>

<style>
html, body, #app {
  height: 100%;
  width: 100%;
}
.green-icon {
  color: #00d1b2;
}
.list-title {
  margin-top: 1.5rem;
}
table {
  width: 100%;
}
</style>
