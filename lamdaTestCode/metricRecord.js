const axios = require('axios');

const getMetirc = async () => {
    const start = new Date().getTime();

    await axios.get('http://localhost:1180/api/helloworld')
    const timeTaken = new Date().getTime() - start;
    return timeTaken;
}

const main = async (num) => {
    const res = await Promise.allSettled(
        Array.from(Array(num)).map(async () => {
            return await getMetirc();
        })
    )
    const results = res.filter(item => item.status === 'fulfilled')
    results.sort((a, b) => a.value - b.value)
    console.log(`
        Request Launched: ${num}
        Request Completed: ${results.length}
        Response Time:
            min: ${results[0].value}
            max: ${results[results.length - 1].value}
            median: ${results[results.length / 2 + 1].value}
        Codes:
            200: ${results.length}
            502: ${num - results.length}
    `)
}

main(200)