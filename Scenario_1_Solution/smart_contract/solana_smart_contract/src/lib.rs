// Import necessary modules from the Solana program library
use solana_program::{
    account_info::AccountInfo,      // Handles accounts that are passed to the program
    entrypoint,                    // Entry point for the Solana program
    entrypoint::ProgramResult,     // Result type used for program execution
    msg,                           // Macro for logging messages
    pubkey::Pubkey,                // Represents a public key
};

// Define the entry point for the Solana program
entrypoint!(process_instruction);

// Implement the function that will be called when the program is invoked
fn process_instruction(
    _program_id: &Pubkey,          // Public key of the program (not used in this function)
    _accounts: &[AccountInfo],    // Array of account information (not used in this function)
    instruction_data: &[u8],      // Data passed with the instruction
) -> ProgramResult {              // Return type indicating success or failure
    // Convert the instruction data from bytes to a UTF-8 string
    // Handle errors if the conversion fails
    let message = std::str::from_utf8(instruction_data).map_err(|_| solana_program::program_error::ProgramError::InvalidInstructionData)?;

    // Log the received message to the Solana blockchain
    msg!("Received weather data: {}", message);

    // Return Ok to indicate successful execution
    Ok(())
}