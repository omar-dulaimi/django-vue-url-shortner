import "./styles/quasar.scss";
import iconSet from "quasar/icon-set/ionicons-v4";
import "@quasar/extras/ionicons-v4/ionicons-v4.css";

import { Notify } from "quasar";

export default {
  config: {
    iconSet,
  },
  plugins: { Notify },
};
