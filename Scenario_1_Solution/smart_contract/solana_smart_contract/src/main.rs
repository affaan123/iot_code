// Import necessary modules from the standard library and Solana crates
use std::io::Read;                  // For reading from files
use std::fs::File;                  // For file operations
use solana_client::rpc_client::RpcClient;  // Solana RPC client to interact with the blockchain
use solana_sdk::{
    commitment_config::CommitmentConfig, // Configuration for transaction commitment
    instruction::{AccountMeta, Instruction}, // Instruction structures for smart contract interactions
    pubkey::Pubkey,                     // Public key type for Solana
    signature::{Keypair, Signer},      // Keypair and Signer for cryptographic operations
    transaction::Transaction,           // Transaction structure for submitting instructions
};
use std::str::FromStr;                // For parsing strings to other types
use serde::{Serialize};              // For serializing data to JSON

// Define a structure for weather data with Serde serialization
#[derive(Serialize)]
struct WeatherData {
    temperature: f32,   // Temperature in degrees Celsius
    humidity: f32,      // Humidity percentage
}

// Main function to execute the program
fn main() {
    // Define the public key of the smart contract program
    let program_id = Pubkey::from_str("2TApVzjDZPuyG8Vi2sYAhmErEMXgHZUPSAWtUiWBN9XD").unwrap();
    
    // Create an RPC client to interact with the Solana blockchain, using the Devnet endpoint
    let rpc_client = RpcClient::new_with_commitment("https://api.devnet.solana.com", CommitmentConfig::confirmed());

    // Load the keypair from a JSON file
    let mut file = File::open("/Users/affaan/my-wallet.json").expect("Failed to open keypair file");
    let mut data = String::new();
    file.read_to_string(&mut data).expect("Failed to read keypair file");

    // Parse the keypair JSON data into a vector of bytes
    let key_bytes: Vec<u8> = serde_json::from_str(&data).expect("Failed to parse JSON");
    
    // Create a Keypair object from the byte data
    let payer = Keypair::from_bytes(&key_bytes).expect("Failed to create keypair from bytes");

    // Create weather data to send to the smart contract
    let weather_data = WeatherData {
        temperature: 25.0, // Example temperature
        humidity: 60.0,    // Example humidity
    };

    // Serialize the weather data into a binary format using bincode
    let instruction_data = bincode::serialize(&weather_data).expect("Failed to serialize weather data");

    // Create an instruction for the smart contract interaction
    let instruction = Instruction {
        program_id,                  // The smart contract's public key
        accounts: vec![AccountMeta::new(payer.pubkey(), true)], // List of accounts involved in the instruction
        data: instruction_data,      // Serialized data to be sent to the smart contract
    };

    // Fetch the latest blockhash for the transaction
    let recent_blockhash = rpc_client.get_latest_blockhash().unwrap();
    
    // Create a transaction with the instruction and sign it with the payer's keypair
    let transaction = Transaction::new_signed_with_payer(
        &[instruction],                // Array of instructions to be executed
        Some(&payer.pubkey()),         // Account to pay for transaction fees
        &[&payer],                     // Array of signers
        recent_blockhash,              // Latest blockhash for transaction
    );

    // Send the transaction and wait for confirmation
    rpc_client.send_and_confirm_transaction(&transaction).unwrap();
    
    // Print a confirmation message to the console
    println!("Weather data sent to the smart contract");
}