<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png" /> -->
    <ItemBoxComponent class="bla" msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
import ItemBoxComponent from "./components/ItemBoxComponent.vue";

export default {
  name: "App",
  components: {
    ItemBoxComponent
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.bla {
  width: 100vw;
}
</style>
