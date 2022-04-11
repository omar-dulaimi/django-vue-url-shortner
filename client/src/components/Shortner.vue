<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md" style="max-width: 350px; width: 350px">
      <q-form @submit="onSubmit" class="q-gutter-md">
        <q-input
          filled
          v-model="url"
          label="Url *"
          hint="Url to shorten"
          lazy-rules
        />

        <div class="flex flex-center">
          <q-btn label="Generate" type="submit" color="primary" />
        </div>
      </q-form>
    </div>
  </q-page>
</template>

<style></style>

<script>
import { useQuasar } from "quasar";
import { ref } from "vue";
import { isValidHttpUrl } from "../utils";

export default {
  url: "Shortner",
  setup() {
    const $q = useQuasar();
    const url = ref(null);

    return {
      url,
      async onSubmit() {
        if (url.value?.length === 0 || !isValidHttpUrl(url.value)) {
          $q.notify({
            color: "red-5",
            textColor: "white",
            icon: "warning",
            message: "You need to enter a valid url",
          });
        } else {
          const res = await fetch("api/gen_short_url", {
            method: "POST",
            headers: {
              "Content-type": "application/json",
            },
            body: JSON.stringify({ originalUrl: url.value }),
          });
          const data = await res.json();

          if (res.status === 201) {
            const dismiss = $q.notify({
              message: `Generated: ${data?.url}`,
              color: "gray",
              timeout: 60 * 1000,
              actions: [
                {
                  label: "Copy",
                  color: "yellow",
                  noDismiss: true,
                  handler: async () => {
                    await navigator.clipboard.writeText(data?.url);
                    url.value = null;
                    dismiss();
                  },
                },
                {
                  label: "Dismiss",
                  color: "white",
                  handler: () => {
                    url.value = null;
                  },
                },
              ],
            });
          } else {
            $q.notify({
              color: "red-5",
              textColor: "white",
              icon: "warning",
              message: "You need to enter a valid url",
            });
          }
        }
      },
    };
  },
};
</script>
