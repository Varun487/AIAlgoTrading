import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    sidenavtoggle: false,
    backtestmain: true,
    backtestreports: [],
    papertrademain: true,
    papertradereports: [],
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
    flipPapertradeMain(state) {
      state.papertrademain = !state.papertrademain;
    },
    setPapertradeReports(state, payload) {
      state.papertradereports = payload;
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
    flipPapertradeMain({ commit }) {
      commit("flipPapertradeMain");
    },
    setPapertradeReports(state) {
      axios
        .get(process.env.VUE_APP_BASE_URL + "api/papertrader/getstrategies/")
        .then((res) => state.commit("setPapertradeReports", res.data))
        .catch((err) => console.log(err));
    },
  },
  getters: {
    getSideNavToggle: (state) => state.sidenavtoggle,
    getBacktestMain: (state) => state.backtestmain,
    getBacktestReports: (state) => state.backtestreports,
    getPapertradeMain: (state) => state.papertrademain,
    getPapertradeReports: (state) => state.papertradereports,
  },
});
