<template>
  <div class="sidebar">
    <transition name="slide">
      <div v-if="$store.getters.getSideNavToggle" class="sidebar-panel">
        <slot>
          <Link link="/" />
        </slot>
        <slot>
          <Link link="/home" name="Home" class="link-item" />
        </slot>
        <slot>
          <Link link="/about" name="About" class="link-item" />
        </slot>
        <slot>
          <Link link="/api" name="REST API Docs" class="link-item" />
        </slot>
		<slot>
          <Link link="/backtest" name="Back Tests" class="link-item" />
        </slot>
      </div>
    </transition>
  </div>
</template>

<script>
import Link from "./Link.vue";

export default {
  name: "SideNavBar",
  components: {
    Link,
  },
};
</script>

<style scoped>
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.4s ease;
}

.slide-enter,
.slide-leave-to {
  transform: translateX(-100%);
  transition: all 150ms ease-in 0s;
}

.sidebar-panel {
  /* overflow-y: auto; */
  background-color: #222222;
  position: fixed;
  height: 100%;
  padding: 10px;
  width: 100px;
}

.link-item {
  padding: 20px;
  cursor: pointer;
}

</style>
