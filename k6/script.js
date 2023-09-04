import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    stages: [
        { duration: '100s', target: 5000 },
        { duration: '100s', target: 5000 },
        { duration: '100s', target: 5500 },
        { duration: '100s', target: 0 }
    ],
};

export default function () {
    const res = http.get('http://192.168.122.1');
    check(res, { 'status was 200': (r) => r.status === 200 });
    sleep(1)
}
