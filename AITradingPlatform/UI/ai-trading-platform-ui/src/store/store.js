import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    sidenavtoggle: false,
    backtestmain: true,
    backtestreports: [],
  },
  mutations: {
    flipSideNavToggle(state) {
      state.sidenavtoggle = !state.sidenavtoggle;
    },
    flipBacktestMain(state) {
      state.backtestmain = !state.backtestmain;
    },
    setBacktestReports(state, payload) {
      state.backtestreports = payload;
    },
  },
  actions: {
    flipSideNavToggle({ commit }) {
      commit("flipSideNavToggle");
    },
    flipBacktestMain({ commit }) {
      commit("flipBacktestMain");
    },
    setBacktestReports(state) {
      axios
        .get(process.env.VUE_APP_BASE_URL + "api/backtester/viewallreports/")
        .then((res) => state.commit("setBacktestReports", res.data))
        .catch((err) => console.log(err));
    },
  },
  getters: {
    getSideNavToggle: (state) => state.sidenavtoggle,
    getBacktestMain: (state) => state.backtestmain,
    getBacktestReports: (state) => state.backtestreports,
  },
});
