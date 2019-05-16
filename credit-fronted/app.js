import axios from 'axios';
import service from './js/service.js'

(function login(){
    'use strict';

    const email = document.querySelector('#exampleInputEmail1');
    const password = document.querySelector('#exampleInputPassword1')
    const btn = document.querySelector('#btnSubtmit')

    btn.addEventListener('click',(e)=>{
        console.log(service.URLAPI)

        axios.post(`${service.URLAPI}login/`,{
            'email': email.value,
            'password': password.value
        })
        .then(data => dataLogin(data))
        .catch(e => console.error('error login'))
    });


    let dataLogin = (data)=>{
        if(service.isvalidStatus(data.status)){
            window.location.href = '/menu.html'
            service.getToken(data.data)
        }else{
            console.error("Error status")
        }
    }

})();