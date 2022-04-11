<template>
  <div class="home">
    <Shortner msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import Shortner from "@/components/Shortner.vue";

export default {
  name: "HomeView",
  components: {
    Shortner,
  },
};
</script>
