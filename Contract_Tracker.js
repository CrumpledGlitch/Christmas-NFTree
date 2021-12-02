const ethers = require('ethers');
const abi = [{...}]
const contractAddress = '0x000...'

const webSocketProvider = new ethers.providers.WebSocketProvider(process.env.ETHEREUM_NODE_URL, process.env.NETWORK_NAME);
const contract = new ethers.Contract(contractAddress, abi, webSocketProvider);

contract.on("Transfer", (from, to, value, event) => {
        console.log({
            from: from,
            to: to,
            value: value.toNumber(),
            data: event
        });
    });
