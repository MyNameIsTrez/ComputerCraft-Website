<template>
  <div class="terminal">
    <div class="scrollbar"></div>
    <div class="searchbar"></div>
    <div class="sorting-buttons"></div>
    <div class="crafting-status-button"></div>
    <ul class="storage">
      <!-- <li class="item-box" v-for="data in $options.item_names" :key="data"> -->
      <!-- <img
          class="item"
          v-lazy="require(`../assets/placeholder_item.png`)"
          v-bind:alt="item.img"
        />
        <div class="count">
          <div class="count-shadow">150K</div>
          <div class="count-regular">150K</div>
        </div> -->
      <!-- {{ console.log(data) }} -->
      <!-- </li> -->

      <!-- <li class="item-box" v-for="(item, index) in items" :key="index">
        <img class="item" v-lazy="getImgUrl(item.img)" v-bind:alt="item.img" />
        <div class="count">
          <div class="count-shadow">150K</div>
          <div class="count-regular">150K</div>
        </div>
        {{ debug(item) }}
      </li> -->
    </ul>
  </div>
</template>

<script>
import ITEM_NAMES_JSON from "../assets/item_names.json";
// import PLACEHOLDER_ITEM_PNG from "../assets/placeholder_item.png";
export default {
  data() {
    return {
      items: [],
      item_names: ITEM_NAMES_JSON,
      //   placeholder_item_png: PLACEHOLDER_ITEM_PNG,
    };
  },
  mounted() {
    const renders = require.context("@/assets/renders", true, /^.*\.png$/);
    renders.keys().map((key) => {
      // './OpenBlocks/elevator@3.png' -> '/OpenBlocks/elevator@3.png'
      this.items.push({ img: key.replace(".", "") });
    });
    console.log(this.item_names);
    // console.log(`Item count: ${this.items.length}`);
  },
  methods: {
    getImgUrl(pic) {
      return require(`../assets/renders${pic}`);
    },
    debug(msg) {
      console.log(msg);
    },
  },
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
  user-select: none;
}

.item {
  padding: 10px;
  width: 150px;
  image-rendering: pixelated;
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