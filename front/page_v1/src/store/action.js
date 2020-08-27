import {FIND_DEVICE} from "./mutation-type";

export default {
    findDevice({commit}, index){
        commit(FIND_DEVICE, index)
    }
}