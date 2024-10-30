
import numpy
from binary_domain import *

class ReedSolomon():
	def __init__(self, k, n, x, pol):
		"""
		Args:
			k (int): dimension des messages à transmettre.
			n (int): taille du bloc que l'on souhaite transmettre.
			x (liste de string de taille n): les points Xi.
			pol (string): polynome irréductible.
		"""
		self.f = BinaryDomains()
		self.t = Translation()
		self.k = k
		self.n = n
		self.x = x
		self.pol = pol

	def _evaluate(self, polynome, x): 
		y = polynome[-1]
		for i in range(len(polynome)-2, -1, -1):
			y = self.f.add( self.f.multiply(y, x, self.pol), polynome[i] ) 
		return y

	def encoding(self, message_original):
		"""
		Encode le message à stocker sous la forme d'une liste comportant n bytes/octets.

		Args:
			message_original (string): Le message original a encodé.
		
		Returns:
			(liste de string de taille n): Le message encodé.
		"""
		return [self._evaluate(self.t.translateToMachine(message_original), xi) for xi in self.x]


	def gaussian_elimination(self, X, AX):
		"""
		Ex: k = 4: retourne les coefficients (di) de la fonction A(Xi) = d0 + d1*Xi + d2*Xi^2 + d3*Xi^3
		en partant de 4 points (Xi,A(Xi)).

		Ce problème est généralisé pour tout k.
		Pour le résoudre -> Effectuer l'élimination de Gauss-Jordan sur le système Vx = a.
		Avec V la matrice de Vandermonde.
		
		Args:
			X (liste de string de taille k): Les points Xi.
			AX (liste de string de taille k): Les points A(Xi).
		
		Returns:
			(liste de string de taille k): Les coefficients (di) de l'interpolation.
		"""
		P = [] 
		for k in range(self.k):
			P.append([])
			P[k].append(self.t.toBinary(1)); cnt = 0; P[k].append(X[k]); sum = self.f.multiply(X[k], X[k], self.pol)
			while cnt != self.k-2:
				P[k].append(sum)
				sum = self.f.multiply(sum, X[k], self.pol); cnt+=1
			P[k].append(AX[k])

		for i in range(self.k):
			for j in range(self.k):
				if i != j:
					r = self.f.multiply(P[j][i], self.f.inverse(P[i][i], self.pol), self.pol)
					for m in range(self.k+1):
						P[j][m] = self.f.add(P[j][m], self.f.multiply(r, P[i][m], self.pol))
		
		return [self.f.multiply(P[i][self.k], self.f.inverse(P[i][i], self.pol), self.pol) for i in range(self.k)]

	def decoding(self, message_corrupted):
		"""
		Décode le message corrompu sous la forme d'une liste comportant k bytes.

		Args:
			message_corrupted (liste de string de taille n): Le message 'corrompu' reçu.
		
		Returns:
			(bool): True s'il est possible de décoder le message corrompu, False sinon.
			(liste de string de taille n): Le message décodé. (si bool = False, alors retourner []).
		"""
		message = [] ; y = []; cnt = 0
		
		for i in range(len(message_corrupted)):
			if not 'x' in message_corrupted[i]:
				message.append(message_corrupted[i])
				y.append(self.x[i])
			else:
				cnt += 1
		if cnt  > (self.n - self.k):
			return False, []
		
		return True, self.t.translateToHuman(self.gaussian_elimination(y, message))