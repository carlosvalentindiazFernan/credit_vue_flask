import axios from 'axios';

'use strict';

/**
 * util service to get data from api 
 */

let service =(()=>{

    const URLAPI = "http://127.0.0.1:5000/api/v1/";
    let auth_token = "33"
    let storage = window.localStorage;


    let setToken = (data)=>{
        storage.setItem('token', data.Token);
    }


    let getToken = ()=>{
        return storage.getItem('token')   
    }

    let isvalidStatus = (status) =>{
        return (status == 200)? true : false
    }

    return{
        getToken,
        setToken,
        auth_token,
        isvalidStatus,
        URLAPI
    };

})();

export default service;