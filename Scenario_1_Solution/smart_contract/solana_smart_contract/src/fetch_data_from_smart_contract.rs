// Import necessary modules from the Solana client and SDK crates
use solana_client::rpc_client::RpcClient;  // RPC client for interacting with the Solana blockchain
use solana_sdk::pubkey::Pubkey;            // Public key type used in Solana
use serde::Deserialize;                   // For deserializing data
use bincode::deserialize;                 // For deserializing binary data
use std::str::FromStr;                    // For parsing strings into other types

// Define a structure to hold the weather data with deserialization capabilities
#[derive(Deserialize, Debug)]
struct WeatherData {
    temperature: f32,  // Temperature value
    humidity: f32,     // Humidity value
}

// Main function to execute the program
fn main() {
    // Create an RPC client to connect to the Solana Devnet
    let rpc_client = RpcClient::new("https://api.devnet.solana.com");
    
    // Define the public key of the Solana account to query
    let account_pubkey = Pubkey::from_str("6n3maEkN5RWaaM4ajNcWVy4TyriVH7j1RX942FroM19t").unwrap();

    // Fetch the account data from the Solana blockchain
    match rpc_client.get_account(&account_pubkey) {
        Ok(account) => {
            // Extract the binary data from the account
            let data = account.data;
            
            // Attempt to deserialize the binary data into a WeatherData structure
            match deserialize::<WeatherData>(&data) {
                Ok(weather_data) => {
                    // Print the deserialized weather data
                    println!("Weather data from smart contract: {:?}", weather_data);
                    
                    // Print individual fields of the weather data
                    println!("Temperature: {}", weather_data.temperature);
                    println!("Humidity: {}", weather_data.humidity);
                },
                Err(_) => println!("Failed to deserialize weather data"), // Handle deserialization error
            }
        },
        Err(e) => println!("Failed to fetch account data: {}", e), // Handle account fetch error
    }
}