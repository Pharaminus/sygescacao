import { useState } from "react";
import { TextInput, View, Text, TouchableOpacity, StyleSheet } from "react-native";
import { CheckBox } from "react-native-web";


const AjouterVente = (params) => {
    const [nomClient, setNomClient] = useState(''); 
    const [nomEntreprise, setNomEntreprise] = useState(''); 
    const [siegeSociale, setSiegeSociale] = useState(''); 
    const [numeroTelephone, setNumeroTelephone] = useState(''); 

    const addVente = () => {

    }

    const [valeur, setValeur] = useState(0);

    const handlePress = (valeur) => {
        setValeur(valeur);
    };


    return(

        <View>
            <View>
                <Text>Gestion de vente</Text>
            </View>
            <TextInput
                placeholder="Nom client"
                value={nomClient}
                onChangeText={setNomClient}
            />
            <TextInput
                placeholder="Nom entreprise"
                value={nomClient}
                onChangeText={setNomClient}
            />
            <TextInput
                placeholder="Siege sociale"
                value={nomClient}
                onChangeText={setNomClient}
            />
            <TextInput
                placeholder="Nom client"
                value={nomClient}
                onChangeText={setNomClient}
            />
            <View>
                <Bouton onPress={handlePress} />
                <Text>Valeur : {valeur}</Text>
            </View>
            
        </View>


    );
}

export default AjouterVente;



const Bouton = () => {
    const [active, setActive] = useState(false);
    const [valeur, setValeur] = useState(0);

    const handlePress = () => {
        setActive(!active);
        setValeur(active ? 0 : 1);
    };

    return (
        <TouchableOpacity
        style={[styles.bouton, active ? styles.active : styles.inactive]}
        onPress={handlePress}
        >
        <Text style={styles.text}>{active ? 'sac 1 ok' : 'sac 1'}</Text>
        </TouchableOpacity>
    );
};

const styles = StyleSheet.create({
    bouton: {
        // padding: "auto",
        borderRadius: 5,
        margin: 10,
        height:30,
        textAlign:"center",
        paddingHorizontal:8
    },
    active: {
        backgroundColor: 'green',
    },
    inactive: {
        backgroundColor: '#ccc',
    },
    text: {
        fontSize: 18,
        color: '#fff',
    },
});








