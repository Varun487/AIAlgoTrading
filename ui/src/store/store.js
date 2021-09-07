import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import JwPagination from 'jw-vue-pagination';
Vue.component('jw-pagination', JwPagination);
import VueZoomer from 'vue-zoomer'


Vue.use(Vuex);
Vue.use(VueZoomer);


export const store = new Vuex.Store({
  state: {
    sidenavtoggle: false,
    allstrategy: {
      mainpage: true,
      strategy: [],
      strategyid: "",
    },
    token: localStorage.getItem('auth_token')|| null,
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
    selected_strategy: undefined,
    all_backtests: {
      mainpage: true,
      all_backtests: [],
      backtestid: "",
    },
    backtest_data:undefined,
    trade_visualization:undefined,
    trades:undefined,
    //i:0,
    
    
    
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
    setSelectedStrategy(state, payload) {
      state.selected_strategy = payload;
    },
    setAllBacktests(state, payload) {
      state.all_backtests.all_backtests = payload;
    },
    flipAllBacktestsMainPage(state) {
      state.all_backtests.mainpage = !state.all_backtests.mainpage;
    },
    setBacktestsId(state, payload) {
      state.all_backtests.backtestid = payload;
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
    setBacktestReportdata(state, payload) {
      state.backtest_data = payload;
    },
    setTradeVisualization(state,payload){
      state.trade_visualization=payload;
    },
    setTrades(state,payload){
      state.trades=payload;
    },
    // incrementRows(state,payload){
    //   state.i+=payload;
      
    // },
    retrieveToken(state,token){
      state.token=token
    }

    
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
    flipPerStrategiesMainPage({ commit }) {
      commit("flipPerStrategiesMainPage");
    },
    flipAllBacktestsMainPage({ commit }) {
      commit("flipAllBacktestsMainPage");
    },
    async setBacktestReportdata(state,id) {
      
      const res = await axios.get(`${process.env.VUE_APP_BASE_URL}api/backtester/backtestdata/${id}/`,{
          headers: {
            'Authorization': ' Token 63cf4515ff99c2635ff560fb9f78e15b57916cb6'

          }
        });
        state.commit("setBacktestReportdata", res.data)
        
    },
    async  setTradeVisualization(state,id) {
      
      const res = await axios.get(`${process.env.VUE_APP_BASE_URL}api/backtester/backtestsignalvisualization/${id}/`,{
          headers: {
            'Authorization': ' Token 63cf4515ff99c2635ff560fb9f78e15b57916cb6'
          }
        });
        state.commit("setTradeVisualization", res.data)
        
    },

    async  setTrades(state,id) {
      
      const res = await axios.get(`${process.env.VUE_APP_BASE_URL}api/backtester/allbacktesttrades/${id}/`,{
          headers: {
            'Authorization': ' Token 63cf4515ff99c2635ff560fb9f78e15b57916cb6'
          }
        });
        state.commit("setTrades", res.data)
      
    },
    
    
    async setAllStrategies(state) {
      /*
      axios
        .get(process.env.VUE_APP_BASE_URL + "api/strategies/allstrategies/")
        .then((res) => state.commit("setAllStrategies", res.data))
        .catch((err) => console.log(err));
      */
     const res = await axios.get(`${process.env.VUE_APP_BASE_URL}api/strategies/allstrategies/`, {
       headers: {
         'Authorization': 'Token 63cf4515ff99c2635ff560fb9f78e15b57916cb6'
       }
     });
     state.commit("setAllStrategies", res.data)
    },
    async setSelectedStrategy(state,id) {
      const res = await axios.get(`${process.env.VUE_APP_BASE_URL}api/strategies/strategydata/${id}/`,{
        headers: {
          'Authorization': 'Token 63cf4515ff99c2635ff560fb9f78e15b57916cb6'
        }
      });
      state.commit("setSelectedStrategy", res.data)
    },
    async setAllBacktests(state,id) {
      const res = await axios.get(`${process.env.VUE_APP_BASE_URL}api/backtester/allbacktests/${id}/`,{
        headers: {
          'Authorization': 'Token 63cf4515ff99c2635ff560fb9f78e15b57916cb6'
        }
      });
      console.log(res.data)
      state.commit("setAllBacktests", res.data)
    },
    setBacktestId({ commit }, payload) {
      commit("setBacktestId", payload);
    },
    setStrategyId({ commit }, payload) {
      commit("setStrategyId", payload);
    },
    setBacktestsId({ commit }, payload) {
      commit("setBacktestsId", payload);
    },
    setselected_strategyId({ commit }, payload) {
      commit("setselected_strategyId", payload);
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
          `${process.env.VUE_APP_BASE_URL}api/backtester/getreportbyid/${id}/`
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
          `${process.env.VUE_APP_BASE_URL}api/backtester/getordersbyreportid/${id}/`
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
    
    
      retrieveToken(context,credentials){

      return new Promise((resolve,reject)=>{ 
      axios.post(process.env.VUE_APP_BASE_URL + "api/auth/token/login/",{
        username: credentials.username,
        password: credentials.password,
      })
      .then(response => {
        const token=response.data.auth_token
        
        localStorage.setItem('auth_token',token)
        context.commit('retrieveToken',token)
        resolve(response)
      })
      .catch(error => {
        console.log(error)
        reject(error)
  
      })
    })
  }
    
    

  },
  getters: {
    getSideNavToggle: (state) => state.sidenavtoggle,
    getPapertradeMain: (state) => state.papertrademain,
    getPapertradeReports: (state) => state.papertradereports,
    // getBacktestsMainPage: (state) => state.backtests.mainpage,
    getBacktestsFilteredReports: (state) => state.backtests.filteredreports,
    getBacktestsReports: (state) => state.backtests.reports,
    getBacktestId: (state) => state.backtests.backtestid,
    getBacktestReportData: (state) => state.backtest_data,
    getBacktestsSummaryLoading: (state) => state.backtests.summaryloading,
    getBacktestsAccountSizeLoading: (state) =>
      state.backtests.accountsizeloading,
    getBacktestsAccountSizes: (state) => state.backtests.accountsizes,
    getBacktestsTimeStamps: (state) => state.backtests.timestamps,
    getAllStrategies: (state) => state.allstrategy.strategy,
    getStrategyId: (state) => state.allstrategy.strategyid,
    getAllStrategiesMainPage: (state) => state.allstrategy.mainpage,
    getSelectedStrategy: (state) => state.selected_strategy,
    getAllBacktests: (state) => state.all_backtests.all_backtests,
    getBacktestsId: (state) => state.all_backtests.backtestid,
    getAllBackTestMainPage: (state) => state.all_backtests.mainpage,
    getTradeVisualization: (state)=> state.trade_visualization,
    getTrades: (state)=> state.trades,
    getToken: (state)=> state.token,
    getloggedIn:(state)=> state.token != null 
    // getincrementRows: (state)=> state.i,
    // getselected_strategyId: (state) => state.selected_strategy.selected_strategyid,
  },
});
