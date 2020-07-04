<template>
  <div class="terminal">
    <div class="scrollbar"></div>
    <div class="searchbar"></div>
    <div class="sorting-buttons"></div>
    <div class="crafting-status-button"></div>
    <ul class="storage">
      <li class="item-box" v-for="(item, index) in items" :key="index">
        <img class="item" v-lazy="getImgUrl(item.img)" v-bind:alt="item.img" />
        <div class="count">
          <div class="count-shadow">150K</div>
          <div class="count-regular">150K</div>
        </div>
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
  font-size: 300%;
  position: relative;
}

.count-shadow {
  position: absolute;
  color: #3f3f3f;
  bottom: 0px;
  right: 14.5px;
}

.count-regular {
  position: absolute;
  color: white;
  bottom: 5px;
  right: 19.5px;
}
</style>