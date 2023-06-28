// const contractAddress = "0x3646ff101beAC4D38F50d37A5C5caaC234cC9A68";
// const web3 = new Web3(
//   new Web3.providers.HttpProvider(
//     `https://sepolia.infura.io/v3/5c84d02cce30471ea955d1e9f6b3117c`,
//   ),
// );
// const contract = new web3.eth.Contract(contract_abi.contract_abi, contractAddress);


if(!sessionStorage.getItem("isFirstTime")){
  sessionStorage.setItem("isFirstTime", true)
  sessionStorage.setItem("isConnected", false)
  sessionStorage.setItem("selectedAddress", null)
}

console.log("is connected = ", sessionStorage.getItem("isConnected"))
console.log("selected address =", sessionStorage.getItem("selectedAddress"))
// Function to handle the connect button click event
async function connectMetamask() {
  try {
    const provider = await detectEthereumProvider();
    if (provider) {
      await ethereum.request({ method: 'eth_requestAccounts' });
      if(sessionStorage.getItem("isConnected") == "false"){
        sessionStorage.isConnected = true;
        const accounts = await provider.request({ method: 'eth_requestAccounts' });
        sessionStorage.selectedAddress = accounts[0];
        console.log('Metamask connected');
        // sepolia network code 
        switchNetwork("0xaa36a7")
      }
      else{
        console.log("already connected")
        return;
      }
      makeConnectButtonColored();
    }
    else{
      console.log('Metamask not detected');
    }
  } catch (error) {
    console.error(error);
  }
}
// console.log(game.wallet_address);
// Function to handle the send transaction button click event
// async function sendTransaction() {
//   // console.log({{game.wallet_address}});
//   if (sessionStorage.getItem("isConnected") == "false") {
//     console.log('Metamask wallet is not connected');
//     return;
//   }
//   const transaction = {
//     from: sessionStorage.selectedAddress,
//     to: '{{ game.wallet_address }}',
//     value: '{{ game.get_price_in_wei16 }}',
//   };

//   try {
//     const transactionHash = await ethereum.request({
//       method: 'eth_sendTransaction',
//       params: [transaction],
//     });
//     console.log('Transaction sent:', transactionHash);
//   } catch (error) {
//     console.error('Error sending transaction:', error);
//   }
// }


async function clearMetaMaskConnection() {
  try {
    if(sessionStorage.getItem("isConnected") == "true"){
      sessionStorage.isConnected = false;
      console.log("Сonnection to metamask terminated")
      makeConnectButtonColored();
    }
    else{
      console.log("already disconnected")
      return;
    }
  } catch (error) {
    console.error(error);
  }
}

function makeConnectButtonColored(){
  const connectButton = document.getElementById('connectButton');
  var metamask_ico = document.createElement("img");
  var child = connectButton.lastElementChild; 
  while (child) {
    connectButton.removeChild(child);
    child = connectButton.lastElementChild;
  }
  if(sessionStorage.getItem("isConnected") == "true"){
    metamask_ico.setAttribute("src", "/static/ico/metamask_on.png");
  }
  else{
    metamask_ico.setAttribute("src", "/static/ico/metamask_off.png");
  }
  metamask_ico.setAttribute("height", "64");
  metamask_ico.setAttribute("width", "64");
  metamask_ico.setAttribute("alt", "metamask_wallet");
  connectButton.appendChild(metamask_ico);
}

async function switchNetwork(chainIdInHex){       
  if (window.ethereum.networkVersion != chainIdInHex) {
    try {
      await window.ethereum.request({
        method: 'wallet_switchEthereumChain',
        params: [{ chainId: "0xaa36a7"}]
      });
    } catch (err) {
      if (err.code == 4902){
        console.log("You don't add the Sepolia network to metamask")
      }
      console.log("error = ", err)
    }
  }
}

// Attach the click event listeners to the buttons
const connectButton = document.getElementById('connectButton');
makeConnectButtonColored();
connectButton.addEventListener('click', connectMetamask);

// const sendTransactionButton = document.getElementById('sendTransactionButton');
// if(sendTransactionButton){
//   sendTransactionButton.addEventListener('click', sendTransaction);
// }

const disconnectButton = document.getElementById('disconnectButton');
disconnectButton.addEventListener('click', clearMetaMaskConnection);
// disconnectButton.addEventListener('click', yourMethod);
