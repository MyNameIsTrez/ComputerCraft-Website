<template>
  <div class="terminal">
    <div class="scrollbar"></div>
    <div class="searchbar"></div>
    <div class="sorting-buttons"></div>
    <div class="crafting-status-button"></div>
    <ul class="storage">
      <li class="item-box" v-for="(item, index) in items" :key="index">
        <img class="item" v-lazy="getImgUrl(item.img)" v-bind:alt="item.img" />
        <div class="count">0</div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: []
    };
  },
  mounted() {
    const renders = require.context("@/assets/renders", true, /^.*\.png$/);
    renders.keys().map(key => {
      // './OpenBlocks/elevator@3.png' -> '/OpenBlocks/elevator@3.png'
      this.items.push({ img: key.replace(".", "") });
    });
    // console.log(`Item count: ${this.items.length}`);
  },
  methods: {
    getImgUrl(pic) {
      return require(`../assets/renders${pic}`);
    }
  }
};
</script>

<style lang="css" scoped>
.storage {
  display: flex;
  flex-flow: row wrap;
  padding: 0;
  margin: 0;
}

.item-box {
  display: flex;
  position: relative;
  background-image: url("../assets/item-box.svg");
}

.item {
  padding: 10px;
  width: 150px;
}

@font-face {
  font-family: minecraft;
  src: url("../assets/fonts/minecraft.otf");
}

.count {
  font-family: minecraft;
  color: white;
  font-size: 300%;
  position: absolute;
  right: 15px;
  bottom: 0px;
}
</style>