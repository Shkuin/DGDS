if(!sessionStorage.getItem("isFirstTime")){
  sessionStorage.setItem("isFirstTime", true)
  sessionStorage.setItem("isConnected", false)
  sessionStorage.setItem("selectedAddress", null)
}

// console.log("is connected = ", sessionStorage.getItem("isConnected"))
// console.log("selected address =", sessionStorage.getItem("selectedAddress"))
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

async function sendTransaction(event){
  async function loadWeb3() {
    if (window.ethereum) {
      window.web3 = new Web3(window.ethereum);
      window.ethereum.enable();
    }
  }
  async function loadBuyGameContract() {
    let abi = contract_abi;
    let address = "0xdef5841caAdEAEe5dF7FEb929bEE3BE27069A297";
    return await new window.web3.eth.Contract(abi, address);
  }
  async function getCustomerAccount() {
    const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
    console.log("account info = ", accounts[0]);
    return accounts[0];
  }

  async function send(devAddress, gameId, gamePrice) {
    await loadWeb3();
    window.contract = await loadBuyGameContract();
    const customer_account = await getCustomerAccount();
    PRIVATE_KEY = "750bb8368c19376f2ddb57f78a4a810bc73789f7845a9f52a7651a444fd8fb84";
    const dgds_developer_account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
    let res = await window.contract.methods.payAndCreateCustomerNFT(devAddress, customer_account, 0, gameId)
         .send({ from: dgds_developer_account.address,
                value: gamePrice,});
    console.log("res = ", res);
  }

  if (typeof window.ethereum !== 'undefined' && sessionStorage.getItem("isConnected") == "false") {
    console.log("fwfwe");
    send(event.currentTarget.devAddress , event.currentTarget.gameId, event.currentTarget.gamePrice);
  }
  else{
    console.log("Something wrong with window.ethereum")
  }
}

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
