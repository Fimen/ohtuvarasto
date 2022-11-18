import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(belf):
        self.varasto = Varasto(10)
        self.varastoneg = Varasto(-5, -3)
        self.varastoyli = Varasto(10, 15)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    
    def test_alkutilavuus_nollataan_jos_annetaan_negatiivinen_tilavuus(self):
        self.assertAlmostEqual(self.varastoneg.tilavuus, 0)

    def test_alkusaldo_nollataan_jos_annetaan_negatiivinen_saldo(self):
        self.assertAlmostEqual(self.varastoneg.saldo, 0)        

    def test_tilavuutta_suurempi_alkusaldo_ei_ole_yli_tilavuuden(self):
        self.assertAlmostEqual(self.varastoyli.saldo, 10)
    
    def test_negatiivisen_maaran_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 8)
    
    def test_tilavuuden_ylittavan_maaran_lisays_asettaa_saldoksi_maksimin(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(5)

        self.assertAlmostEqual(self.varasto.saldo, 10)
    	
    def test_negatiivisen_maaran_ottaminen_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(8)
        tulos = self.varasto.ota_varastosta(-5)
        
        self.assertAlmostEqual(tulos, 0)
    	
    def test_ylisuuren_maaran_ottaminen_palauttaa_saldon(self):
        self.varasto.lisaa_varastoon(8)
        
        self.assertAlmostEqual(self.varasto.ota_varastosta(15), 8)
    	
    def test_tulostaminen_antaa_oikeat_maarat(self):
        self.varasto.lisaa_varastoon(8)

        tulos = str(self.varasto)
        self.assertEqual(tulos, 'saldo = 8, vielä tilaa 2')
