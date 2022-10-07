namespace PND {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Diagnostics;
    open Microsoft.Quantum.Measurement;
    
    //@EntryPoint()
    operation Sample() : Unit {
        use reg = Qubit[2];
        X(reg[1]);
        DumpMachine();
        ResetAll(reg);
    }

    @EntryPoint()
    operation Stage1(shots: Int): Result[][] {
        mutable results = [[Zero], size = shots];
        for i in 0..(shots - 1) {
            let partial = QRAMInitialization();
            set results w/= i <- partial;
        }

        return results;
    }

    //@EntryPoint()
    operation QRAMInitialization() : Result[] {
        // Initializates the quantum circuit by means of qRAM algorithm

        //// INITIALIZATION
        use address = Qubit[3];
        use data = Qubit[4];

        // Boolean encoding of binary conversion for addresses: [0,1,2,3,4] -> [000, 001, 010, 011, 100] -> 0 = false && 1 = true
        let address_enc = [[false, false, false], [false, false, true], [false, true, false], [false, true, true], [true, false, false]];
        // Boolean encoding of binary conversion for unused addresses: [5,6,7] -> [101, 110, 111] -> 0 = false && 1 = true
        let unused_enc = [[true, false, true], [true, true, false], [true, true, true]];
        // Boolean encoding of binary conversion for data: [1,3,5,7,9] -> [0001, 0011, 0101, 0111, 1001] -> 0 = false && 1 = true
        let data_enc = [[false, false, false, true], [false, false, true, true], [false, true, false, true], [false, true, true, true], [true, false, false, true]];

        //// QRAM ALGORITHM
        for qubit in address {
            H(qubit);
        }

        // qRAM columns
        for i in 0..(Length(address_enc) - 1) {
            (ControlledOnBitString(address_enc[i], EncodeOnBitString))(address, (data, data_enc[i]));
        }
        
        // unwanted addresses conversion
        for i in 0..(Length(unused_enc) - 1) {
            (ControlledOnBitString(unused_enc[i], EncodeOnBitString))(address, (data, data_enc[i]));
        }

        //// MEASUREMENT
        let result = [M(data[0]), M(data[1]), M(data[2]), M(data[3])];
        ResetAll(address + data);
        return result;
    }

    operation EncodeOnBitString(data: Qubit[], bits: Bool[]) : Unit is Adj + Ctl {
        // Encodes the Boolean bitstring over the qubits passed as data
        for i in 0..(Length(bits) - 1) {
            if (bits[i] == true) {
                X(data[i]);
            }
        }
    }
}
