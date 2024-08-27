import React, { useState, useEffect } from 'react';
import { Button, Modal, ModalBody } from 'reactstrap';
import { FaBars, FaTimes } from 'react-icons/fa';
import JsxParser from 'react-jsx-parser'
import './index.css';
import axios from 'axios';
import LogoManaus from "./Logo-prefeitura-de-manaus-preto-removebg-preview.png"
import DropdownCustom from './Components/DropDownCompononent';
import 'bootstrap/dist/css/bootstrap.min.css';

const Tab = ({ title, activeTab, index, onClick }) => (
  <div
    className={`tab ${activeTab === index ? 'active' : ''}`}
    onClick={() => onClick(index)}
  >
    {title}
  </div>
);

const TabContainer = ({ tabs, activeTab, onClick }) => {
  return (
    <div className="tabs">
      {tabs.map((tab, index) => (
        <Tab
          key={index}
          title={tab.title}
          activeTab={activeTab}
          index={index}
          onClick={onClick}
        />
      ))}
    </div>
  );
};

const App = () => {
  const HOST = "http://localhost:5000"

  const [idhData, setIDHData] = useState([]);
  const [popData, setPOPData] = useState([]);
  const [iiData, setIIData] = useState([]);

  // Coleta dados de saúde do Back-End
  const [healthData, setHealthData] = useState([]);
  const [healthDataYear, setHealthDataYear] = useState([]);
  const [healthDataFont, setHealthDataFont] = useState([]);

  // Coleta dados de educação do Back-End
  const [educationData, setEducationData] = useState([]);
  const [educationDataYear, setEducationDataYear] = useState([]);
  const [educationDataFont, setEducationDataFont] = useState([]);


  // Coleta dados de renda do Back-End
  const [incomeData, setIncomeData] = useState([]);
  const [incomeDataYear, setIncomeDataYear] = useState([]);
  const [incomeDataFont, setIncomeDataFont] = useState([]);

  const [modalActive, setModalActive] = useState(false);
  const [modalMsg, setModalMsg] = useState("");

  const [modalSaudeIsOpen, setModalSaudeIsOpen] = React.useState(false);
  const [modalSaudeMsg, setModalSaudeMsg] = useState("");

  const [modalEducacaoIsOpen, setModalEducacaoIsOpen] = React.useState(false);
  const [modalEducacaoMsg, setModalEducacaoMsg] = useState("");

  const [modalRendaIsOpen, setModalRendaIsOpen] = React.useState(false);
  const [modalRendaMsg, setModalRendaMsg] = useState("");



  // const [isAdvanced, setIsAdvanced] = useState(true);

  // parte para download de arquivos (exemplo), trocar pelo verdadeiro da API.
  const handleDownload = async () => {
    const anoInput = document.getElementById('anoInput');
    const contextDropdown = document.getElementById('contextDropdown');
    const opcaoDropdown = document.getElementById('opcaoDropdown');

    const ano = anoInput?.value;
    const contexto = contextDropdown?.value;
    const opcao = opcaoDropdown?.value;


    // Simulação da chamada à API e download do arquivo
    // 
    try {
      // Obtém os dados da API simulada
      const fetchData = async () => {

        if (ano < 2008 || ano > 2023)
          return "O ano mínimo é 2008 e o máximo é 2023"

        if (contexto === '')
          return "Selecione uma opção válida"

        if (opcao === undefined)
          return "Selecione uma opção válida"

        const response = await fetch('http://localhost:5000/Download-Files?year='
          + ano + '&context=' + contexto + '&filename=' + opcao)

        return await response.text();
      }

      const data = await fetchData();

      // A VARIAVEL DATA É A RESPOSTA QUE DEVE APARECER NO MODAL
      // console.log('Resposta:', data);

      setModalMsg(data);
      toggleModal();

    } catch (error) {
      console.error('Erro ao obter os dados da API:', error);
    }
  };

  const toggleModal = () => {
    setModalActive(!modalActive);
  }


  useEffect(() => {
    axios.get(HOST + '/Idh')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setIDHData(response.data);
      })
      .catch(error => {
        console.error('Erro na requisição de IDH:', error);
      });

    axios.get(HOST + '/Populacao')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setPOPData(response.data);
      })
      .catch(error => {
        console.error('Erro na requisição de Populacao:', error);
      });

    axios.get(HOST + '/Ii')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setIIData(response.data);
      })
      .catch(error => {
        console.error('Erro na requisição de II:', error);
      });

    // Faz a requisição para a API de Saúde
    axios.get(HOST + '/Saude/1')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setHealthData(response);
      })
      .catch(error => {
        console.error('Erro na requisição de Saúde:', error);
      });

    axios.get(HOST + '/Saude/1?year=true')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setHealthDataYear(response.data);
      })
      .catch(error => {
        console.error('Erro na requisição de Saúde:', error);
      });

    axios.get(HOST + '/Saude/1/Info?font=true')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setHealthDataFont(response.data);
      })
      .catch(error => {
        console.error('Erro na requisição de Saúde:', error);
      });

    axios.get(HOST + '/Saude/1/Info?dict=true')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setModalSaudeMsg(response.data);
      })
      .catch(error => {
        console.error('Erro na requisição de Saúde:', error);
      });

    // Faz a requisição para a API de Educação
    axios.get(HOST + '/Educacao/1')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setEducationData(response);
      })
      .catch(error => {
        console.error('Erro na requisição de Educação:', error);
      });

    axios.get(HOST + '/Educacao/1?year=true')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setEducationDataYear(response.data);
      })
      .catch(error => {
        console.error('Erro na requisição de Educação:', error);
      });


    axios.get(HOST + '/Educacao/1/Info?font=true')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setEducationDataFont(response.data);
      })
      .catch(error => {
        console.error('Erro na requisição de Educação:', error);
      });

    axios.get(HOST + '/Educacao/1/Info?dict=true')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setModalEducacaoMsg(response.data);
      })
      .catch(error => {
        console.error('Erro na requisição de Educação:', error);
      });

    // Faz a requisição para a API de Renda
    axios.get(HOST + '/Renda/1')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setIncomeData(response);
      })
      .catch(error => {
        console.error('Erro na requisição de Renda:', error);
      });

    axios.get(HOST + '/Renda/1?year=true')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setIncomeDataYear(response.data);
      })
      .catch(error => {
        console.error('Erro na requisição de Renda:', error);
      });

    axios.get(HOST + '/Renda/1/Info?font=true')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setIncomeDataFont(response.data);
      })
      .catch(error => {
        console.error('Erro na requisição de Renda:', error);
      });

    axios.get(HOST + '/Renda/1/Info?dict=true')
      .then(response => {
        // Armazena os dados recebidos no estado do componente
        setModalRendaMsg(response.data);
      })
      .catch(error => {
        console.error('Erro na requisição de Renda:', error);
      });

  }, []);

  // const [dadosDaAPI, setDadosDaAPI] = useState([]);

  // useEffect(() => {
  //   // Função assíncrona para obter os dados da API
  //   const fetchData = async () => {
  //     try {
  //       // Fazer a chamada à API e obter os dados
  //       const response = await fetch('URL_DA_API');
  //       const data = await response.json();

  //       // Atualizar o estado com os dados obtidos da API
  //       setDadosDaAPI(data);
  //     } catch (error) {
  //       console.error('Erro ao obter os dados da API:', error);
  //     }
  //   };

  //   // Chamar a função para obter os dados da API
  //   fetchData();
  // }, []);

  const toggleModalSaude = () => {
    setModalSaudeIsOpen(!modalSaudeIsOpen);
  };

  const toggleModalEducacao = () => {
    setModalEducacaoIsOpen(!modalEducacaoIsOpen);
  };

  const toggleModalRenda = () => {
    setModalRendaIsOpen(!modalRendaIsOpen);
  }

  const onHealthPrevInfoBtnClick = (data) => {
    if (data.request.responseURL.at(-1) > 1) {
      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) - Number(1)).toString())
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setHealthData(response);
        })
        .catch(error => {
          console.error('Erro na requisição de Saúde:', error);
        });

      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) - Number(1)).toString()
        + '?year=true')
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setHealthDataYear(response.data);
        })
        .catch(error => {
          console.error('Erro na requisição de Saúde:', error);
        });

      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) - Number(1)).toString()
        + '/Info?font=true')
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setHealthDataFont(response.data);
        })
        .catch(error => {
          console.error('Erro na requisição de Saúde:', error);
        });

      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) - Number(1)).toString()
        + '/Info?dict=true')
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setModalSaudeMsg(response.data);
        })
        .catch(error => {
          console.error('Erro na requisição de Saúde:', error);
        });
    }
  };

  const onHealthNextInfoBtnClick = (data) => {
    if (data.request.responseURL.at(-1) < 2) {
      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) + Number(1)).toString())
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setHealthData(response);
        })
        .catch(error => {
          console.error('Erro na requisição de Saúde:', error);
        });

      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) + Number(1)).toString()
        + '?year=true')
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setHealthDataYear(response.data);
        })
        .catch(error => {
          console.error('Erro na requisição de Saúde:', error);
        });

      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) + Number(1)).toString()
        + '/Info?font=true')
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setHealthDataFont(response.data);
        })
        .catch(error => {
          console.error('Erro na requisição de Saúde:', error);
        });

      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) + Number(1)).toString()
        + '/Info?dict=true')
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setModalSaudeMsg(response.data);
        })
        .catch(error => {
          console.error('Erro na requisição de Saúde:', error);
        });
    }
  };

  const onEducationPrevInfoBtnClick = (data) => {
    if (data.request.responseURL.at(-1) > 1 || data.request.responseURL.split('/').at(-2) === '2') {
      let url = data.request.responseURL


      if (data.request.responseURL.split('/').at(-1) === 'Aprovacao') {
        url = data.request.responseURL.slice(0, -11) + (Number(data.request.responseURL.slice(0, -10).at(-1)) - Number(1)).toString()
      }
      // if(data.request.responseURL.split('/').at(-1) === '1'){
      //   url = data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) + Number(1)).toString()
      // }

      if (url.split('/').at(-2) === '2' || data.request.responseURL.split('/').at(-2) === '2') {
        if (url.split('/').at(-1) === 'Abandono') {
          axios.get(url.split('/').slice(0, -1).join('/') + '/Reprovacao')
            .then(response => {
              // Armazena os dados recebidos no estado do componente
              setEducationData(response);
            })
            .catch(error => {
              console.error('Erro na requisição de Educação:', error);
            });
          axios.get(url
            + '?year=true')
            .then(response => {
              // Armazena os dados recebidos no estado do componente
              setEducationDataYear(response.data);
            })
            .catch(error => {
              console.error('Erro na requisição de Educação:', error);
            });
        }
        else if (data.request.responseURL.split('/').at(-1) === "Reprovacao") {
          axios.get(url.slice(0, -11) + '/Aprovacao')
            .then(response => {
              // Armazena os dados recebidos no estado do componente
              setEducationData(response);
            })
            .catch(error => {
              console.error('Erro na requisição de Educação:', error);
            });
          axios.get(url
            + '?year=true')
            .then(response => {
              // Armazena os dados recebidos no estado do componente
              setEducationDataYear(response.data);
            })
            .catch(error => {
              console.error('Erro na requisição de Educação:', error);
            });
        }
        else if (data.request.responseURL.split('/').at(-1) === "Aprovacao") {
          axios.get(url)
            .then(response => {
              // Armazena os dados recebidos no estado do componente
              setEducationData(response);
            })
            .catch(error => {
              console.error('Erro na requisição de Educação:', error);
            });
          axios.get(url
            + '?year=true')
            .then(response => {
              // Armazena os dados recebidos no estado do componente
              setEducationDataYear(response.data);
            })
            .catch(error => {
              console.error('Erro na requisição de Educação:', error);
            });
        }
      }
      if (url.split('/').at(-2) === '2') {
        axios.get(url.split('/').slice(0, -1).join("/")
          + '/Info?font=true')
          .then(response => {
            // Armazena os dados recebidos no estado do componente
            setEducationDataFont(response.data);
          })
          .catch(error => {
            console.error('Erro na requisição de Educação:', error);
          });

        axios.get(url.split('/').slice(0, -1).join("/")
          + '/Info?dict=true')
          .then(response => {
            // Armazena os dados recebidos no estado do componente
            setModalEducacaoMsg(response.data);
          })
          .catch(error => {
            console.error('Erro na requisição de Educação:', error);
          });
      }
      else {
        axios.get(url
          + '/Info?font=true')
          .then(response => {
            // Armazena os dados recebidos no estado do componente
            setEducationDataFont(response.data);
          })
          .catch(error => {
            console.error('Erro na requisição de Educação:', error);
          });

        axios.get(url
          + '/Info?dict=true')
          .then(response => {
            // Armazena os dados recebidos no estado do componente
            setModalEducacaoMsg(response.data);
          })
          .catch(error => {
            console.error('Erro na requisição de Educação:', error);
          });
      }
    }
  };

  const onEducationNextInfoBtnClick = (data) => {
    if (data.request.responseURL.at(-1) < 2 || data.request.responseURL.split('/').at(-2) === '2') {
      let url = data.request.responseURL

      // if(data.request.responseURL.split('/').at(-1) === 'Abandono'){
      //   url = data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) + Number(1)).toString()
      // }
      if (data.request.responseURL.split('/').at(-1) === '1') {
        url = data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) + Number(1)).toString()
      }

      if (url.at(-1) === '2' || url.split('/').at(-2) === '2') {
        if (url.at(-1) === '2') {
          axios.get(url + '/Aprovacao')
            .then(response => {
              // Armazena os dados recebidos no estado do componente
              setEducationData(response);
            })
            .catch(error => {
              console.error('Erro na requisição de Educação:', error);
            });
          axios.get(url + '/Aprovacao'
            + '?year=true')
            .then(response => {
              // Armazena os dados recebidos no estado do componente
              setEducationDataYear(response.data);
            })
            .catch(error => {
              console.error('Erro na requisição de Educação:', error);
            });
        }
        else if (data.request.responseURL.split('/').at(-1) === "Aprovacao") {
          axios.get(url.slice(0, -10) + '/Reprovacao')
            .then(response => {
              // Armazena os dados recebidos no estado do componente
              setEducationData(response);
            })
            .catch(error => {
              console.error('Erro na requisição de Educação:', error);
            });
          axios.get(url
            + '?year=true')
            .then(response => {
              // Armazena os dados recebidos no estado do componente
              setEducationDataYear(response.data);
            })
            .catch(error => {
              console.error('Erro na requisição de Educação:', error);
            });
        }
        else if (data.request.responseURL.split('/').at(-1) === "Reprovacao") {
          axios.get(url.slice(0, -11) + '/Abandono')
            .then(response => {
              // Armazena os dados recebidos no estado do componente
              setEducationData(response);
            })
            .catch(error => {
              console.error('Erro na requisição de Educação:', error);
            });
          axios.get(url
            + '?year=true')
            .then(response => {
              // Armazena os dados recebidos no estado do componente
              setEducationDataYear(response.data);
            })
            .catch(error => {
              console.error('Erro na requisição de Educação:', error);
            });
        }
      }
      if (url.split('/').at(-2) === '2') {
        axios.get(url.split('/').slice(0, -1).join("/")
          + '/Info?font=true')
          .then(response => {
            // Armazena os dados recebidos no estado do componente
            setEducationDataFont(response.data);
          })
          .catch(error => {
            console.error('Erro na requisição de Educação:', error);
          });

        axios.get(url.split('/').slice(0, -1).join("/")
          + '/Info?dict=true')
          .then(response => {
            // Armazena os dados recebidos no estado do componente
            setModalEducacaoMsg(response.data);
          })
          .catch(error => {
            console.error('Erro na requisição de Educação:', error);
          });
      }
      else {
        axios.get(url
          + '/Info?font=true')
          .then(response => {
            // Armazena os dados recebidos no estado do componente
            setEducationDataFont(response.data);
          })
          .catch(error => {
            console.error('Erro na requisição de Educação:', error);
          });

        axios.get(url
          + '/Info?dict=true')
          .then(response => {
            // Armazena os dados recebidos no estado do componente
            setModalEducacaoMsg(response.data);
          })
          .catch(error => {
            console.error('Erro na requisição de Educação:', error);
          });
      }
    }
  };

  const onIncomePrevInfoBtnClick = (data) => {
    if (data.request.responseURL.at(-1) > 1) {
      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) - Number(1)).toString())
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setIncomeData(response);
        })
        .catch(error => {
          console.error('Erro na requisição de Renda:', error);
        });

      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) - Number(1)).toString()
        + '?year=true')
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setIncomeDataYear(response.data);
        })
        .catch(error => {
          console.error('Erro na requisição de Renda:', error);
        });

      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) - Number(1)).toString()
        + '/Info?font=true')
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setIncomeDataFont(response.data);
        })
        .catch(error => {
          console.error('Erro na requisição de Renda:', error);
        });

      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) - Number(1)).toString()
        + '/Info?dict=true')
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setModalRendaMsg(response.data);
        })
        .catch(error => {
          console.error('Erro na requisição de Renda:', error);
        });
    }
  };

  const onIncomeNextInfoBtnClick = (data) => {
    if (data.request.responseURL.at(-1) < 3) {
      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) + Number(1)).toString())
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setIncomeData(response);
        })
        .catch(error => {
          console.error('Erro na requisição de Renda:', error);
        });

      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) + Number(1)).toString()
        + '?year=true')
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setIncomeDataYear(response.data);
        })
        .catch(error => {
          console.error('Erro na requisição de Renda:', error);
        });

      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) + Number(1)).toString()
        + '/Info?font=true')
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setIncomeDataFont(response.data);
        })
        .catch(error => {
          console.error('Erro na requisição de Renda:', error);
        });

      axios.get(data.request.responseURL.slice(0, -1) + (Number(data.request.responseURL.at(-1)) + Number(1)).toString()
        + '/Info?dict=true')
        .then(response => {
          // Armazena os dados recebidos no estado do componente
          setModalRendaMsg(response.data);
        })
        .catch(error => {
          console.error('Erro na requisição de Renda:', error);
        });
    }
  };

  const tabs = [
    {
      title: 'Saúde',
      content: (
        <div className='saude'>
          <div className='cabecalho-saude bg-red-500'>
            <div className='label-esquerdo'>
              <div className='label-edu1'>
                <label htmlFor="idhLabel">IDH: </label>
                <input type="text" id="idhLabel" value={idhData} readOnly />
              </div>
              <div className='label-edu2'>
                <label htmlFor="populacaoLabel">População: </label>
                <input type="text" id="populacaoLabel" value={popData} readOnly />
              </div>
            </div>
            <h2 className="text-2xl">SAÚDE</h2>
            <div className='label-direito'>
              <label htmlFor="iiLabel">II: </label>
              <input type="text" id="iiLabel" value={iiData} readOnly />
            </div>
          </div>
          <div className='body-saude relative'>
            <div className="w-full h-full text-2xl flex justify-center items-center overflow-auto pb-5">
              {healthData.data}

            </div>
            <div className='absolute bottom-0 right-0'>
              <Button color="warning" className='mb-3 mr-5' onClick={toggleModalSaude}>Dicionário</Button>
              <Modal isOpen={modalSaudeIsOpen} toggle={toggleModalSaude}>
                <ModalBody>
                  {modalSaudeMsg === "" ? "Dicionário indisponível" : modalSaudeMsg}
                </ModalBody>
              </Modal>
            </div>
          </div>
          <div className='footer-saude'>
            <div className='space-x-4'>
              <Button color='danger'
                onClick={() => onHealthPrevInfoBtnClick(healthData)}
              >Informação Anterior</Button>
              <Button color='danger'>Ano Anterior</Button>
            </div>
            <div className='flex-col'>
              <div className='ano-saude'>
                <label htmlFor="ano-saude">Ano: </label>
                <input type="text" id="ano-saude" value={healthDataYear} readOnly />
              </div>
              <div className='ano-saude'>
                <label htmlFor="ano-saude">Fonte: </label>
                <input type="text" id="ano-saude" value={healthDataFont} readOnly />
              </div>
            </div>
            <div className='space-x-4'>

              <Button color='danger'>Próximo Ano</Button>
              <Button color='danger'
                onClick={() => onHealthNextInfoBtnClick(healthData)}
              >Próxima Informação</Button>
            </div>

          </div>
        </div>
      ),
    },
    {
      title: 'Educação',
      content: (
        <div className='educacao'>
          <div className='cabecalho-educacao bg-sky-500'>
            <div className='label-esquerdo'>
              <div className='label-edu1'>
                <label htmlFor="idhLabel">IDH: </label>
                <input type="text" id="idhLabel" value={idhData} readOnly />
              </div>
              <div className='label-edu2'>
                <label htmlFor="populacaoLabel">População: </label>
                <input type="text" id="populacaoLabel" value={popData} readOnly />
              </div>
            </div>
            <h2 className="text-2xl">EDUCAÇÃO</h2>
            <div className='label-direito'>
              <label htmlFor="iiLabel">II: </label>
              <input type="text" id="iiLabel" value={iiData} readOnly />
            </div>
          </div>
          <div className='body-educacao relative'>
            <div className='h-full w-full overflow-auto pb-5'>
              <JsxParser jsx={educationData.data} />
            </div>
            <div className='absolute bottom-0 right-0'>
              <Button color="warning" className='mb-3 mr-5' onClick={toggleModalEducacao}>Dicionário</Button>
              <Modal isOpen={modalEducacaoIsOpen} toggle={toggleModalEducacao}>
                <ModalBody>
                  <p>{modalEducacaoMsg === "" ? "Dicionário indisponível" : modalEducacaoMsg}</p>
                </ModalBody>
              </Modal>
            </div>
          </div>
          <div className='footer-educacao'>

            <div className='space-x-4'>
              <Button color='primary'
                onClick={() => onEducationPrevInfoBtnClick(educationData)}
              >Informação Anterior</Button>
              <Button color='primary'>Ano Anterior</Button>
            </div>
            <div className='flex-col'>
              <div className='ano-educacao'>
                <label htmlFor="ano-educacao">Ano: </label>
                <input type="text" id="ano-educacao" value={educationDataYear} readOnly />
              </div>
              <div className='ano-educacao'>
                <label htmlFor="ano-educacao">Fonte: </label>
                <input type="text" id="ano-educacao" value={educationDataFont} readOnly />
              </div>
            </div>
            <div className='space-x-4'>
              <Button color='primary'>Próximo Ano</Button>
              <Button color='primary'
                onClick={() => onEducationNextInfoBtnClick(educationData)}
              >Próxima Informação</Button>
            </div>
          </div>

        </div>
      ),
    },
    {
      title: 'Renda',
      content: (
        <div className='renda'>
          <div className='cabecalho-renda bg-emerald-500'>
            <div className='label-esquerdo'>
              <div className='label-edu1'>
                <label htmlFor="idhLabel">IDH: </label>
                <input type="text" id="idhLabel" value={idhData} readOnly />
              </div>
              <div className='label-edu2'>
                <label htmlFor="populacaoLabel">População: </label>
                <input type="text" id="populacaoLabel" value={popData} readOnly />
              </div>
            </div>
            <h2 className="text-2xl">RENDA</h2>
            <div className='label-direito'>
              <label htmlFor="iiLabel">II: </label>
              <input type="text" id="iiLabel" value={iiData} readOnly />
            </div>
          </div>
          <div className='body-renda relative'>
            <div className='w-full h-full text-2xl flex justify-center items-center overflow-auto pb-5'>
              {
                incomeData.request?.responseURL.at(-1) === '3' &&
                <>
                  <iframe src={incomeData.request?.responseURL} className='w-full h-full'>
                    <p>Your browser does not support iframes.</p>
                  </iframe>
                </>
              }
              {
                incomeData.request?.responseURL.at(-1) !== '3' &&
                <>
                  {incomeData.data}
                </>
              }
            </div>
            <div className='absolute bottom-0 right-0'>
              <Button color="warning" className='mb-3 mr-5' onClick={toggleModalRenda}>Dicionário</Button>
              <Modal isOpen={modalRendaIsOpen} toggle={toggleModalRenda}>
                <ModalBody>
                  <p>{modalRendaMsg === "" ? "Dicionário indisponível" : modalRendaMsg}</p>
                </ModalBody>
              </Modal>
            </div>
          </div>
          <div className='footer-renda'>
            <div className='space-x-4'>
              <Button color='success'
                onClick={() => onIncomePrevInfoBtnClick(incomeData)}
              >Informação Anterior</Button>
              <Button color='success'>Ano Anterior</Button>
            </div>
            <div className='flex-col'>
              <div className='ano-renda'>
                <label htmlFor="ano-renda">Ano: </label>
                <input type="text" id="ano-renda" value={incomeDataYear} readOnly />
              </div>
              <div className='ano-renda'>
                <label htmlFor="ano-renda">Fonte: </label>
                <input type="text" id="ano-renda" value={incomeDataFont} readOnly />
              </div>
            </div>
            <div className='space-x-4'>
              <Button color='success'>Próximo Ano</Button>
              <Button color='success'
                onClick={() => onIncomeNextInfoBtnClick(incomeData)}
              >Próxima Informação</Button>
            </div>
          </div>

        </div>
      ),
    },
    {
      title: 'Baixar dados',
      content: (
        <div className='body-dados ml-5'>
          <header className='text-4xl mb-12 mt-3'> Baixar Dados </header>
          <div className='w-4/6'>
            <h5 className='mb-4'>
              Nessa página você pode baixar e integrar automaticamente dados de outros períodos ao sistema
              IDH Measurer para uma visualização melhor e mais completa das análises feitas.
            </h5>
            <label htmlFor="anoInput">Informe o ano: </label>
            <br />
            <input type="text" id="anoInput" />
          </div>
          <div>
            <DropdownCustom></DropdownCustom>
            <button className="baixar mt-2" onClick={handleDownload}>Baixar Arquivo</button>
            <Modal isOpen={modalActive} toggle={toggleModal} centered className='text-lg font-bold'>
              <ModalBody>{modalMsg}</ModalBody>
            </Modal>
          </div>
        </div>
      ),
    },
  ];

  const [activeTab, setActiveTab] = useState(0);
  const [sidebarVisible, setSidebarVisible] = useState(true);

  const handleTabClick = (index) => {
    setActiveTab(index);
  };

  const handleToggleSidebar = () => {
    setSidebarVisible(!sidebarVisible);
  };

  useEffect(() => {
    const resizeHandler = () => {
      const sidebar = document.querySelector('.sidebar');
      const windowHeight = window.innerHeight;
      sidebar.style.height = `${windowHeight}px`;
    };


    window.addEventListener('load', resizeHandler);
    window.addEventListener('resize', resizeHandler);

    return () => {
      window.removeEventListener('load', resizeHandler);
      window.removeEventListener('resize', resizeHandler);
    };
  }, []);

  return (
    <div className="app-container">
      <div className={`sidebar ${sidebarVisible ? '' : 'hidden'}`}>
        <h1>IDH MEASURER</h1>
        <img src={LogoManaus} alt="Logo" className="logo" />
        <TabContainer tabs={tabs} activeTab={activeTab} onClick={handleTabClick} />
        <footer class="sidebar-footer">
          <p>&copy; 2023 DevBoys</p>
        </footer>
      </div>
      <div className="main-container">
        <button className="toggle-button" onClick={handleToggleSidebar}>
          {sidebarVisible ? <FaTimes /> : <FaBars />}
        </button>
        <div className="main-content">
          {/* <h1>{tabs[activeTab].title}</h1> */}
          {tabs[activeTab].content}

        </div>
      </div>
    </div>
  );
};

export default App;