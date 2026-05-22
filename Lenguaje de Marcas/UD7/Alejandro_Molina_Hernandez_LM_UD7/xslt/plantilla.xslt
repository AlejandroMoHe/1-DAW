<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="html" encoding="UTF-8" indent="yes" />

    <xsl:template match="/">
        <html>
            <head>
                <meta charset="UTF-8" />
                <title>Estudios de Cine</title>
            </head>
            <body>
                <h1>Listado de Estudios de Cine</h1>

                <table border="1">
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Fundadores</th>
                        <th>Fundación</th>
                        <th>Activo</th>
                        <th>Ingresos</th>
                        <th>Última actualización</th>
                    </tr>

                    <xsl:for-each select="estudios/estudio">
                        <tr>
                            <td>
                                <xsl:value-of select="id" />
                            </td>
                            <td>
                                <xsl:value-of select="nombre" />
                            </td>
                            <td>
                                <xsl:for-each select="fundadores/fundador">
                                    <xsl:value-of select="." />
<xsl:if test="position()!=last()">, </xsl:if>
                                </xsl:for-each>
                            </td>
                            <td>
                                <xsl:value-of select="fechaFundacion" />
                            </td>
                            <td>
                                <xsl:value-of select="activo" />
                            </td>
                            <td>
                                <xsl:value-of select="ingresosMillones" />
                            </td>
                            <td>
                                <xsl:value-of select="ultimaActualizacion" />
                            </td>
                        </tr>
                    </xsl:for-each>

                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>