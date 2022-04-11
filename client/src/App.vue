<template>
  <q-layout view="hHh LpR fFf">
    <q-header reveal elevated class="bg-primary text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg" />
          </q-avatar>
          Url Shortner
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <Shortner />
    </q-page-container>

    <q-footer reveal elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title class="flex flex-center text-subtitle1">
          Made by Omar Dulaimi
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>
;

<script>
import { ref } from "vue";
import Shortner from "./components/Shortner.vue";

export default {
  name: "LayoutDefault",

  components: {
    Shortner,
  },

  setup() {
    return {
      leftDrawerOpen: ref(false),
    };
  },
};
</script>
