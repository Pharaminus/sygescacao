// RegisterScreen.js
import React, { useState } from 'react';
import { View, TextInput, Button, Text, StyleSheet, TouchableOpacity } from 'react-native';

const Inscription = () => {
    const [nom, setNom] = useState('');
    const [mot_de_passe, setMot_de_passe] = useState('');
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');

    const handleRegister = async () => {

        try {
            
            const response = await fetch('http://192.168.43.8:8000/inscription', {
                
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ nom, mot_de_passe, email }),
            });

            
            
            const data = await response.json();
            if (response.ok) {
                setMessage('Inscription réussie !');
            } else {
                setMessage(data.error || 'Erreur lors de l\'inscription.');
            }
        } catch (error) {
            console.log('====================================');
            console.log(error);
            console.log('====================================');
            setMessage('Erreur de connexion.');
        }
    };

    return (
        <View>
            <View>
                <Text  style={ styles.titre}>CocoaTrace</Text>
            </View>
            <View style={styles.container}>
                <Text style={styles.titre}>Inscription</Text>
                <TextInput
                    style={styles.input}
                    placeholder="Nom d'utilisateur"
                    value={nom}
                    onChangeText={setNom}
                />
                <TextInput
                    style={styles.input}
                    placeholder="Email"
                    value={email}
                    onChangeText={setEmail}
                    keyboardType="email-address"
                />
                <TextInput
                    style={styles.input}
                    placeholder="Mot de passe"
                    value={mot_de_passe}
                    onChangeText={setMot_de_passe}
                    secureTextEntry
                />
                {/* <Button title="S'inscrire" onPress={handleRegister} s/> */}
                <TouchableOpacity style={styles.bouton} onPress={handleRegister}>
                    <Text style={styles.boutonTexte}>S'inscrire</Text>
                </TouchableOpacity>
                {message ? <Text style={styles.message}>{message}</Text> : null}
            </View>
        </View>
    );
};

const styles = StyleSheet.create({
    main:{

    },
    container: {
        justifyContent: 'center',
        alignItems: 'center',
        padding:"auto",
        height:600,
    },
        input: {
        width: 300,
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        padding: 10,
        marginBottom: 10,
  },
    message: {
        marginTop: 12,
        textAlign: 'center',
    },
    bouton: {
        backgroundColor: '#4CAF50',
        padding: 10,
        borderRadius: 5,
    },
    boutonTexte: {
        color: '#fff',
        fontSize: 18,
    },
    titre: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
    textAlign:"center",
  },
});

export default Inscription;