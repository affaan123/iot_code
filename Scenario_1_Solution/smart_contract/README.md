This README provides instructions to deploy a smart contract to the Solana blockchain and execute Rust scripts to interact with the deployed contract.

Prerequisites

Before you begin, ensure you have the following tools installed:

	•	Rust: Follow the official guide here to install Rust.
	•	Solana CLI: Install the Solana CLI by following the instructions here.

Step 1: Set Up Solana CLI

	1.	Configure Solana CLI:
	solana config set --url https://api.devnet.solana.com

	2.	Generate a Keypair:
	solana-keygen new --outfile ~/.config/solana/id.json

	3.	Airdrop SOL to your account:
	solana airdrop 2

	Step 2: Compile the Smart Contract

	1.	Navigate to the Contract(lib.rs) Directory:
	2.	Build the Contract:
	cargo build-bpf --manifest-path=Cargo.toml --bpf-out-dir=target/deploy
	3.	Generate the Deployable File:
	Ensure your target/deploy folder contains the *.so file, which is your compiled smart contract.

Step 3: Deploy the Smart Contract

	1.	Deploy the Contract:
	solana program deploy target/deploy/your_smart_contract.so

	2.	Note the Program ID:
	After deploying, note down the program ID printed in the console. You’ll need this for interacting with the contract.


Step 4: Interact with the Smart Contract Using Rust Scripts

main.rs - Interacting with the Smart Contract

	1.	Configure Your Program ID and Network:
	In src/main.rs, ensure you specify the correct program ID and network endpoint.
	2.	Execute the Script:
	Run the script using Cargo:
	cargo run --bin main

	fetch_data_from_smart_contract.rs - Fetching Data from the Smart Contract

	1.	Modify Program ID and Network (if needed):
	Make sure the program ID and network are correctly configured in fetch_data_from_smart_contract.rs.
	2.	Execute the Script:
	Run the script using Cargo:
	cargo run --bin fetch_data_from_smart_contract

Additional Notes

	•	Ensure all dependencies are included in Cargo.toml.
	•	Make sure the Solana CLI is correctly configured to connect to the desired network (e.g., Devnet, Testnet, Mainnet).
	•	If the deployment fails, check the Solana version compatibility with your contract.
	•	Ensure your Rust environment is up-to-date.
	•	Verify the network endpoint is reachable and you have enough SOL for deployment.