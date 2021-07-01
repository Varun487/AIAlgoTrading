import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    sidenavtoggle: false,
    allstrategy: {
      mainpage: true,
      strategy: [],
      strategyid: "",
    },
    papertrademain: true,
    papertradereports: [],
    backtests: {
      mainpage: true,
      reports: [],
      filteredreports: [],
      backtestid: "",
      summaryloading: false,
      accountsizeloading: false,
      backtestreportdata: {},
      backtestorders: [],
      accountsizes: [],
      timestamps: [],
    },
    strategydata: {
      mainpage: true,
      strategy_id: "",
      strategy_name: "",
      strategy_desc:"",
      stock_selection: "",
      exit_criteria: "",
      stop_loss_method: "",
      take_profit_method: "",
    },
  },
  mutations: {
    flipSideNavToggle(state) {
      state.sidenavtoggle = !state.sidenavtoggle;
    },
    flipBacktestsMainPage(state) {
      state.backtests.mainpage = !state.backtests.mainpage;
    },
    flipAllStrategiesMainPage(state) {
      state.allstrategy.mainpage = !state.allstrategy.mainpage;
    },
    setBacktestsReports(state, payload) {
      state.backtests.reports = payload;
      state.backtests.filteredreports = payload;
    },
    setBacktestId(state, payload) {
      state.backtests.backtestid = payload;
    },
    setAllStrategies(state, payload) {
      state.allstrategy.strategy = payload;
    },
    setStrategyId(state, payload) {
      state.allstrategy.strategyid = payload;
    },
    resetBacktestId(state) {
      state.backtests.backtestid = null;
    },
    setFilteredBacktestsReports(state, payload) {
      state.backtests.filteredreports = payload;
    },
    resetFilteredBacktestReports(state) {
      state.backtests.filteredreports = state.backtests.reports;
    },
    setReportInfo(state, data) {
      state.backtests.backtestreportdata = data;
    },
    setOrdersData(state, data) {
      state.backtests.backtestorders = data;
      state.backtests.accountsizes = [];
      state.backtests.timestamps = [];
      data.map((order) => {
        state.backtests.accountsizes.push(order.account_size);
        state.backtests.timestamps.push(new Date(order.order.time_stamp));
      });
      state.backtests.accountsizeloading = false;
    },
    flipPapertradeMain(state) {
      state.papertrademain = !state.papertrademain;
    },
    setPapertradeReports(state, payload) {
      state.papertradereports = payload;
    },
    setPerStrategyId(state, payload) {
      state.strategydata.strategy_id = payload;
    },
    setStrategyName(state, payload) {
      state.strategydata.strategy_name = payload;
    },
    setStrategyDesc(state, payload) {
      state.strategydata.strategy_desc = payload;
    },
    setStrategyStockSelection(state, payload) {
      state.strategydata.stock_selection = payload;
    },
    setExitCriteria(state, payload) {
      state.strategydata.exit_criteria = payload;
    },
    setStopLoss(state, payload) {
      state.strategydata.stop_loss_method = payload;
    },
    setTakeProfit(state, payload) {
      state.strategydata.take_profit_method = payload;
    },
  },
  actions: {
    flipSideNavToggle({ commit }) {
      commit("flipSideNavToggle");
    },
    flipBacktestsMainPage({ commit }) {
      commit("flipBacktestsMainPage");
    },
    flipAllStrategiesMainPage({ commit }) {
      commit("flipAllStrategiesMainPage");
    },
    setBacktestsReports(state) {
      axios
        .get(process.env.VUE_APP_BASE_URL + "api/backtester/viewallreports/")
        .then((res) => state.commit("setBacktestsReports", res.data))
        .catch((err) => console.log(err));
    },
    setAllStrategies(state) {
      axios
        .get(process.env.VUE_APP_BASE_URL + "api/strategies/allstrategies/")
        .then((res) => state.commit("setAllStrategies", res.data))
        .catch((err) => console.log(err));
    },
    setBacktestId({ commit }, payload) {
      commit("setBacktestId", payload);
    },
    setStrategyId({ commit }, payload) {
      commit("setStrategyId", payload);
    },
    setFilteredBacktestsReports({ commit }, payload) {
      commit("setFilteredBacktestsReports", payload);
    },
    resetFilteredBacktestReports({ commit }) {
      commit("resetFilteredBacktestReports");
    },
    setReportInfo({ commit }, id) {
      this.state.backtests.summaryloading = true;
      axios
        .get(
          `${process.env.VUE_APP_BASE_URL}api/backtester/getreportbyid/${id}`
        )
        .then((res) => {
          commit("setReportInfo", res.data[0]);
          this.state.backtests.summaryloading = false;
        })
        .catch((err) => console.log(err));
    },
    setOrdersData({ commit }, id) {
      this.state.backtests.accountsizeloading = true;
      axios
        .get(
          `${process.env.VUE_APP_BASE_URL}api/backtester/getordersbyreportid/${id}`
        )
        .then((res) => {
          commit("setOrdersData", res.data);
        })
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
    setStrategyName(state) {
      axios
        .get(process.env.VUE_APP_BASE_URL + "api/strategies/strategydata/2/")
        .then((res) => state.commit("setStrategyName", res.data))
        .catch((err) => console.log(err));
    },
    setPerStrategyId({ commit }, payload) {
      commit("setPerStrategyId", payload);
    },
  },
  getters: {
    getSideNavToggle: (state) => state.sidenavtoggle,
    getPapertradeMain: (state) => state.papertrademain,
    getPapertradeReports: (state) => state.papertradereports,
    getBacktestsMainPage: (state) => state.backtests.mainpage,
    getBacktestsFilteredReports: (state) => state.backtests.filteredreports,
    getBacktestsReports: (state) => state.backtests.reports,
    getBacktestId: (state) => state.backtests.backtestid,
    getBacktestReportData: (state) => state.backtests.backtestreportdata,
    getBacktestsSummaryLoading: (state) => state.backtests.summaryloading,
    getBacktestsAccountSizeLoading: (state) =>
      state.backtests.accountsizeloading,
    getBacktestsAccountSizes: (state) => state.backtests.accountsizes,
    getBacktestsTimeStamps: (state) => state.backtests.timestamps,
    getAllStrategies: (state) => state.allstrategy.strategy,
    getStrategyId: (state) => state.allstrategy.strategyid,
    getAllStrategiesMainPage: (state) => state.allstrategy.mainpage,
  },
});
