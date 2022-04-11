<template>
  <div class="q-pa-md row justify-center items-center about-wrapper">
    <q-card class="about-card">
      <q-tabs v-model="tab" class="text-teal">
        <q-tab label="Description" name="one" />
        <q-tab label="Author" name="two" />
        <q-tab label="Tech Stack" name="three" />
      </q-tabs>
      <q-separator />

      <q-tab-panels v-model="tab" animated>
        <q-tab-panel name="one">
          Generate a short link from any valid url. Links will be deleted after
          10 days.
          <q-card-actions align="right">
            <q-btn
              flat
              icon="ion-logo-github"
              size="1.2rem"
              href="https://github.com/omar-dulaimi"
              target="_blank"
              no-caps
            >
              <span class="text-subtitle1"> Source Code </span>
            </q-btn>
          </q-card-actions>
        </q-tab-panel>

        <q-tab-panel name="two">
          My name is Omar Dulaimi(obviously!), and I'm a full stack engineer. I
          build open source stuff and love trying new and trendy technologies.
          You can find more about what I do using these links:
          <q-card-actions align="right">
            <q-btn
              flat
              round
              icon="ion-logo-linkedin"
              size="1.2rem"
              href="https://www.linkedin.com/in/omar-dulaimi"
              target="_blank"
            />
            <q-btn
              flat
              round
              icon="ion-logo-github"
              size="1.2rem"
              href="https://github.com/omar-dulaimi"
              target="_blank"
            />
            <q-btn
              flat
              round
              size="1.2rem"
              href="https://dev.to/omardulaimi"
              target="_blank"
            >
              <q-icon>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  aria-label="dev.to"
                  role="img"
                  viewBox="0 0 512 512"
                >
                  <rect width="512" height="512" rx="15%" />
                  <path
                    fill="#fff"
                    d="M140.47 203.94h-17.44v104.47h17.45c10.155-.545 17.358-8.669 17.47-17.41v-69.65c-.696-10.364-7.796-17.272-17.48-17.41zm45.73 87.25c0 18.81-11.61 47.31-48.36 47.25h-46.4V172.98h47.38c35.44 0 47.36 28.46 47.37 47.28zm100.68-88.66H233.6v38.42h32.57v29.57H233.6v38.41h53.29v29.57h-62.18c-11.16.29-20.44-8.53-20.72-19.69V193.7c-.27-11.15 8.56-20.41 19.71-20.69h63.19zm103.64 115.29c-13.2 30.75-36.85 24.63-47.44 0l-38.53-144.8h32.57l29.71 113.72 29.57-113.72h32.58z"
                  />
                </svg>
              </q-icon>
            </q-btn>
          </q-card-actions>
        </q-tab-panel>

        <q-tab-panel
          name="three"
          class="full-width column wrap justify-center items-center content-center"
        >
          <img src="/static/assets/django.png" height="75" />
          <q-separator dark />
          <img src="/static/assets/django-rest-framework.png" height="120" />
          <q-separator dark />
          <img src="/static/assets/sqllite.png" height="100" />
          <q-separator dark />
          <img src="/static/assets/vuejs.png" height="125" />
          <q-separator dark />
          <img src="/static/assets/quasar.png" height="175" />
        </q-tab-panel>
      </q-tab-panels>
    </q-card>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    return {
      tab: ref("one"),
    };
  },
};
</script>

<style scoped>
.about-wrapper {
  height: calc(100vh - 100px) !important;
}
.about-card {
  width: 100%;
  max-width: 500px;
}
</style>
