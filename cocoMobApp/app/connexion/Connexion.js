
import React, { useState } from 'react';
import { ViewComponent } from 'react-native';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

const Connexion = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [erreur, setErreur] = useState(null);

  const handleConnexion = async () => {
    try {
      // Appeler l'API de connexion
      const response = await fetch('(link unavailable)', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      const données = await response.json();

      if (données.success) {
        // Connexion réussie, rediriger vers la page principale
        navigation.navigate('/accueil');
      } else {
        setErreur(données.message);
      }
    } catch (error) {
      setErreur('Erreur de connexion');
    }
  };

  return (
    <View style={styles.main}>
      <View>
        <Text  style={ styles.titre}>CocoaTrace</Text>
      </View>
      <View style={styles.container}>
        <Text style={styles.titre}>Connexion</Text>
        <TextInput
          style={styles.input}
          placeholder="Adresse e-mail"
          value={email}
          onChangeText={(text) => setEmail(text)}
        />
        <TextInput
          style={styles.input}
          placeholder="Mot de passe"
          secureTextEntry={true}
          value={password}
          onChangeText={(text) => setPassword(text)}
        />
        {erreur && <Text style={styles.erreur}>{erreur}</Text>}
        <TouchableOpacity style={styles.bouton} onPress={handleConnexion}>
          <Text style={styles.boutonTexte}>Se connecter</Text>
        </TouchableOpacity>
        
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  main:{
    

  },
  container: {
    // flex: 2,
    justifyContent: 'center',
    alignItems: 'center',
    padding:"auto",
    height:600,
  },
  titre: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
    textAlign:"center",
  },
  input: {
    width: 300,
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    padding: 10,
    marginBottom: 10,
  },
  erreur: {
    color: 'red',
    marginBottom: 10,
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
});

export default Connexion;
