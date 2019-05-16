import axios from 'axios';
import service from './js/service.js'

(function login() {
    'use strict';

    const email = document.querySelector('#exampleInputEmail1');
    const password = document.querySelector('#exampleInputPassword1')
    const btn = document.querySelector('#btnSubtmit')

    const listCredit = document.querySelector('#listCredits')

    /**
     * Create Credit
     */
    const formCreate = document.querySelector('#formCreate')
    const companyInput = document.querySelector('#companyInput')
    const companyNumberInput = document.querySelector('#companyNumberInput')
    const creditInput = document.querySelector('#creditInput')
    const btnSubtmitCreate = document.querySelector('#btnSubtmitCreate')


    if (btn) {
        btn.addEventListener('click', (e) => {
            console.log(service.URLAPI)

            axios.post(`${service.URLAPI}login/`, {
                'email': email.value,
                'password': password.value
            })
                .then(data => dataLogin(data))
                .catch(e => console.error('error login'))
        });
    }


    let dataLogin = (data) => {
        if (service.isvalidStatus(data.status)) {
            window.location.href = '/menu.html'
            service.setToken(data.data)
        } else {
            console.error("Error status")
        }
    }

    if (listCredit) {
        console.log(service.getToken())
        axios
            .get(`${service.URLAPI}credits/`, {
                headers: {
                    Authorization: service.getToken()
                }
            })
            .then(response => {
                console.log('Data: ', response.data);
            })
            .catch(error => {
                console.error('An error occurred:', error);
            });
    }

    if (formCreate) {
        let credit = {
            'nameCompany': companyInput.value,
            'numberCompany': companyNumberInput.value,
            'credit': creditInput.value,
            headers: {
                Authorization: service.getToken()
            }
        }
        
        btnSubtmitCreate.addEventListener('click', (e) => {
            console.log(credit)
            axios
                .post(`${service.URLAPI}credits/`, credit)
                .then(response => {
                    console.log('Data: ', response.data);
                })
                .catch(error => {
                    console.error('An error occurred:', error);
                });

        });
    }

})();