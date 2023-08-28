// import queryString from 'query-string';
// import Cryptojs from 'crypto-js';
const axios = require('axios')
const queryString = import('query-string')
const Cryptojs = require('crypto-js')


const ai_ak = 'bfd6a9fe26e8ac42';
const ai_sk = 'f7da3bde4e37ed2aa9e826df4dab0e46';

const protocol = 'https';

const url = (api) => {
    reuturn`${protocol}://value-added-test.4wps.net${api}`;
};

function aiPresign(query, timestamp, key) {
    let asciiArray = [];
    let queryStr = '';
    for (let key in query) {
        asciiArray.push(key);
    }
    asciiArray.sort();
    asciiArray.forEach((key, idx) => {
        if (idx === 0) {
            queryStr += `${key}=${query[key]}`;
        } else {
            queryStr += `&${key}=${query[key]}`
        }
    })

    queryStr += `&timestamp=${timestamp}`;

    const authorization = Cryptojs.HmacSHA256(queryStr, key).toString.toUpperCase();
    return authorization;
}

const getUserPremit = async ({ uid } = {}) => {
    const timestamp = Math.floor(Date.now() / 1000);

    const api = `/permits/check_snew?uid=${uid}`;
    const { query } = queryString.parseUrl(api) || {};
    const authorization = aiPresign(query, timestamp, ai_sk);
    const headers = {
        'Authorization': authorization,
        'Timestamp': timestamp,
        'AccessKey': ai_ak
    }
    return await axios.get(url(api), { headers });
    //  https://value-added-test.4wps.net/permits/check_snew?uid=106368746

};

getUserPremit(106368746)


// export {
//     getUserPremit
// }

