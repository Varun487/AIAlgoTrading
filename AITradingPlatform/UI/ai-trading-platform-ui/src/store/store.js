import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    sidenavtoggle: false,
    backtests: {
      mainpage: true,
      reports: [],
      filteredreports: [],
      backtestid: null,
    },
  },
  mutations: {
    flipSideNavToggle(state) {
      state.sidenavtoggle = !state.sidenavtoggle;
    },
    flipBacktestsMainPage(state) {
      state.backtests.mainpage = !state.backtests.mainpage;
    },
    setBacktestsReports(state, payload) {
      state.backtests.reports = payload;
      state.backtests.filteredreports = payload;
    },
    filterBacktestsReportsByStartDate(state, payload) {
      console.log(payload);
    },
    filterBacktestsReportsByEndDate(state, payload) {
      console.log(payload);
    },
    filterBacktestsReportsByMaxRisk(state, payload) {
      console.log(payload);
    },
    setBacktestId(state, payload) {
      state.backtests.backtestid = payload;
    },
    resetBacktestId(state) {
      state.backtests.backtestid = null;
    },
  },
  actions: {
    flipSideNavToggle({ commit }) {
      commit("flipSideNavToggle");
    },
    flipBacktestsMainPage({ commit }) {
      commit("flipBacktestsMainPage");
    },
    setBacktestsReports(state) {
      axios
        .get(process.env.VUE_APP_BASE_URL + "api/backtester/viewallreports/")
        .then((res) => state.commit("setBacktestsReports", res.data))
        .catch((err) => console.log(err));
    },
    filterBacktestsReportsByStartDate({ commit }, payload) {
      commit("filterBacktestReportsByStartDate", payload);
    },
    filterBacktestsReportsByEndDate({ commit }, payload) {
      commit("filterBacktestReportsByEndDate", payload);
    },
    filterBacktestsReportsByMaxRisk({ commit }, payload) {
      commit("filterBacktestReportsByMaxRisk", payload);
    },
    filterBacktestsReportsByCompany({ commit }, payload) {
      commit("filterBacktestReportsByCompany", payload);
    },
    filterBacktestsReportsByStrategy({ commit }, payload) {
      commit("filterBacktestReportsByStrategy", payload);
    },
    filterBacktestsReportsByDimension({ commit }, payload) {
      commit("filterBacktestReportsByDimension", payload);
    },
    filterBacktestsReportsByTimePeriod({ commit }, payload) {
      commit("filterBacktestReportsByTimePeriod", payload);
    },
    setBacktestId({ commit }, payload) {
      commit("setBacktestId", payload);
    },
  },
  getters: {
    getSideNavToggle: (state) => state.sidenavtoggle,
    getBacktestsMainPage: (state) => state.backtests.mainpage,
    getBacktestsFilteredReports: (state) => state.backtests.filteredreports,
    getBacktestsReports: (state) => state.backtests.reports,
    getBacktestId: (state) => state.backtests.backtestid,
  },
});
