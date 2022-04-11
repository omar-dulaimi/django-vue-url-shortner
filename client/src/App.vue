<template>
  <q-layout view="hHh LpR fFf">
    <q-header reveal elevated class="bg-primary text-white">
      <q-toolbar class="text-white shadow-2 rounded-borders">
        <q-toolbar-title>
          <q-avatar>
            <span class="material-icons"> link </span>
          </q-avatar>
          Url Shortner
        </q-toolbar-title>
        <q-tabs shrink stretch>
          <q-route-tab name="tab1" label="Home" to="/" exact />
          <q-route-tab name="tab2" label="About" to="/about" exact />
        </q-tabs>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view></router-view>
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
import Shortner from "./components/Shortner.vue";

export default {
  name: "LayoutDefault",
  components: {
    Shortner,
  },
};
</script>
